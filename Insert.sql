CREATE PROCEDURE sp_InsertCustomerInfoAndCreateAccount
    
    -- Parameters for cust_info
    @cust_id int,
    @cust_secondary_id varchar(10),
    @first_name nvarchar(200),
    @middle_name nvarchar(200) = NULL,
    @last_name nvarchar(200),
    @suffix varchar(3) IS NULL,
    @date_of_birth date,
    @client_since date = NULL,
    
    -- Parameters for cust_contact
    @cust_email nvarchar(200),
    @cust_phone_home varchar(15),
    @cust_phone_business varchar(15) = NULL,
    @cust_address varchar(200),
    @cust_address_2 varchar(200) = NULL,
    @cust_city varchar(85),
    @cust_state tinyint,
    @cust_zip int,
    @cust_country smallint,

    -- Parameters for cust_emp
    @employment_status bit,
    @employer_name varchar(200),
    @occupation varchar(500),

    -- Parameters for cust_id
    @id_type tinyint,
    @id_state tinyint,
    @id_num varchar(25),
    @id_exp varchar(25),
    @mothers_maiden nvarchar(200),

    -- Parameters for cust_privacy
    @voice_auth bit,
    @do_not_call bit,
    @share_affiliates bit,

    -- Parameters for cust_tax
    @cust_tax_id varchar(25),

    -- Parameters for acct_info
    @acct_id int,
    @acct_num bigint,
    @initial_contact_method tinyint,
    @acct_type tinyint,
    @registration_name varchar(100),
    @acct_activity tinyint,
    @acct_funding tinyint,
    @acct_objective tinyint,
    @acct_purpose tinyint,
    @acct_nickname varchar(50) = NULL,
    @acct_restriction tinyint,
    @acct_status bit,
    @closed_date date,
    @rep_id varchar(5) = NULL,

    -- Parameters for acct_bal
    @acct_bal decimal(18,2),

    -- Parameters for acct_bene
    @acct_bene_id int = NULL,
    @bene_cust_secondary_id varchar(10) = NULL,
    @bene_first_name nvarchar(50) = NULL,
    @bene_last_name nvarchar(50) = NULL,
    @bene_tax_id varchar(50) = NULL,
    @relationship_id tinyint = NULL,
    @bene_portion decimal(5, 2) = NULL,

    -- Parameters for acct_branch
    @acct_branch_id smallint,
    
    -- Parameters for acct_contact
    @contact_name varchar(50),
    @contact_address varchar(50),
    @contact_address_2 varchar(50),
    @contact_city varchar(50),
    @contact_state tinyint,
    @contact_zip int,

    -- Parameters for acct_holders
    @acct_holder_id int,
    @cust_secondary_id varchar(10),

    -- Parameters for acct_jurisdiction
    @jurisdiction_country smallint,
    @justisdiction_state tinyint,

    -- Parameters for acct_limit
    @atm_limit tinyint = 1,
    @ach_limit tinyint = 1,
    @wire_limit tinyint = 1,

    -- Parameters for acct_mobile
    @online bit = 0,
    @mobile bit = 0,
    @two_factor bit = 0,
    biometrics bit = 0,

    -- Parameters for acct_pass
    @acct_pass varchar(50) = NULL,

    --Parameters for acct_poa
    @acct_poa_id int = NULL,
    @poa_cust_secondary_id varchar(10) = NULL,
    @poa_first_name nvarchar(200) = NULL,
    @poa_last_name nvarchar(200) = NULL,
    @poa_tax_id varchar(50),
    @poa_id tinyint = NULL

AS
BEGIN
    -- Declare a variable to capture errors
    DECLARE @error_state INT = 0;
    DECLARE @retry_count INT = 0;

    -- Start the transaction
    BEGIN TRANSACTION;

    BEGIN TRY

        RETRY:
            -- Limit the number of retries to avoid infinite loop
            IF @retry_count >= 50
                THROW 50000, 'Exceeded maximum retry attempts for generating unique Cust IDs', 1;

            -- Generate random numbers
            SET @acct_num = CAST(FLOOR(RAND() * (9999999999 - 1000000000 + 1) + 1000000000) AS BIGINT);
            SET @cust_secondary_id = FORMAT(CAST(FLOOR(RAND() * (999999999 - 100000 + 1) + 100000) AS BIGINT), '0000000000');

            -- Check for uniqueness of account number
            IF EXISTS (SELECT 1 FROM acct_info WHERE acct_num = @acct_num)
            BEGIN
                SET @retry_count = @retry_count + 1;
                GOTO RETRY;
            END;

            -- Check for uniqueness of customer secondary ID
            IF EXISTS (SELECT 1 FROM cust_info WHERE cust_secondary_id = @cust_secondary_id)
            BEGIN
                SET @retry_count = @retry_count + 1;
                GOTO RETRY;
            END;
        
        -- Set client_since as today's date
        IF @client_since IS NULL
            SET @client_since = CAST(GETDATE() AS DATE);

        -- If @rep_id is NULL, set it to the current user's ID
        IF @rep_id IS NULL
            SET @rep_id = SUSER_NAME();

        -- Pre-validation check for cust_info
        IF (@first_name IS NULL OR
            @last_name IS NULL OR
            @date_of_birth IS NULL
            @client_since IS NULL)
        BEGIN
            THROW 50000, 'Mandatory customer info fields missing', 1;
            RETURN;
        END

        -- Insert into cust_info
        INSERT INTO cust_info (cust_id,
                               cust_secondary_id,
                               first_name,
                               middle_name,
                               last_name,
                               suffix,
                               date_of_birth,
                               client_since)
        VALUES (@cust_id,
                @cust_secondary_id,
                @first_name,
                @middle_name,
                @last_name,
                @suffix,
                @date_of_birth,
                @client_since);

        -- Pre-validation check for cust_contact
        IF (@cust_email IS NULL OR 
            @cust_phone_home IS NULL OR 
            @cust_address IS NULL OR
            @cust_city IS NULL OR
            @cust_state IS NULL OR
            @cust_zip IS NULL OR
            @cust_country IS NULL OR
            NOT (@cust_email LIKE '%@%.%'))
        BEGIN
            THROW 50000, 'Mandatory customer contact fields missing', 1;
            RETURN;
        END

        -- Insert into cust_contact
        INSERT INTO cust_contact (cust_id,
                                  cust_email,
                                  cust_phone_home,
                                  cust_phone_business,
                                  cust_address,
                                  cust_address_2,
                                  cust_city,
                                  cust_state,
                                  cust_zip,
                                  cust_country)
        VALUES (@cust_id,
                @cust_email,
                @cust_phone_home,
                @cust_phone_business,
                @cust_address,
                @cust_address_2,
                @cust_city,
                @cust_state,
                @cust_zip,
                @cust_country);
        
        -- Conditionally insert into cust_emp
        IF (@cust_id IS NOT NULL,
            @employment_status IS NOT NULL,
            @employer_name IS NOT NULL,
            @occupation IS NOT NULL)
        
        BEGIN
               
            -- Insert into cust_emp
            INSERT INTO cust_emp (cust_id,
                                    employment_status,
                                    employer_name,
                                    occupation)
            VALUES (@cust_id,
                    @employment_status,
                    @employer_name,
                    @occupation);
        END

        -- Pre-validation check for cust_id
        IF (@id_type IS NULL OR
            @id_state IS NULL OR
            @id_num IS NULL OR
            @id_exp IS NULL OR
            @mothers_maiden IS NULL)
        BEGIN
            THROW 50000, 'Mandatory customer id fields missing', 1;
            RETURN;
        END

        -- Insert into cust_id
        INSERT INTO cust_id (cust_id,
                             id_type,
                             id_state,
                             id_num,
                             id_exp,
                             mothers_maiden)
        VALUES (@cust_id,
                @id_type,
                @id_state,
                @id_num,
                @id_exp,
                @mothers_maiden);

        -- Insert into cust_privacy
        INSERT INTO cust_privacy (cust_id,
                                  voice_auth,
                                  do_not_call,
                                  share_affiliates)
        VALUES (@cust_id,
                @voice_auth,
                @do_not_call,
                @share_affiliates);
        
        -- Pre-validation check for cust_tax
        IF (@cust_tax_id IS NULL)
        BEGIN
            THROW 50000, 'Mandatory customer tax fields missing', 1;
            RETURN;
        END

        -- Insert into cust_tax
        INSERT INTO cust_tax (cust_id, 
                              cust_tax_id)
        VALUES (@cust_id,
                @cust_tax_id);

        -- Pre-validation check for acct_info
        IF (@cust_tax_id IS NULL)
        BEGIN
            THROW 50000, 'Mandatory account information fields missing', 1;
            RETURN;
        END
        
        IF (@initial_contact_method IS NULL OR
            @acct_type
            @registration_name
            @acct_activity
            @acct_funding
            @acct_objective
            @acct_purpose
            @cust_id
            @acct_nickname
            @client_since
            @acct_restriction
            @acct_status
            @closed_date)

        -- Insert into acct_info
        INSERT INTO acct_info (acct_id,
                               acct_num,
                               initial_contact_method,
                               acct_type,
                               registration_name,
                               acct_activity,
                               acct_funding,
                               acct_objective,
                               acct_purpose,
                               cust_id,
                               acct_nickname,
                               client_since,
                               acct_restriction,
                               acct_status,
                               closed_date,
                               rep_id)
        VALUES (@acct_id,
                @acct_num,
                @initial_contact_method,
                @acct_type,
                @registration_name,
                @acct_activity,
                @acct_funding,
                @acct_objective,
                @acct_purpose,
                @cust_id,
                @acct_nickname,
                @client_since,
                @acct_restriction,
                @acct_status,
                @closed_date,
                @rep_id);

        -- Insert into acct_contact
        INSERT INTO acct_contact (acct_id,
                                  contact_name,
                                  contact_address,
                                  contact_address_2,
                                  contact_city,
                                  contact_state,
                                  
                                  contact_zip)
        VALUES (@acct_id,
                @contact_name,
                @contact_address,
                @contact_address_2,
                @contact_city,
                @contact_state,
                @contact_zip);

        -- Conditionally insert into acct_bene
        IF (@acct_bene_id IS NOT NULL AND
            @acct_id IS NOT NULL AND
            @bene_cust_secondary_id IS NOT NULL AND
            @bene_first_name IS NOT NULL AND
            @bene_last_name IS NOT NULL AND
            @bene_tax_id IS NOT NULL AND
            @relationship_id IS NOT NULL AND
            @bene_portion IS NOT NULL)

        BEGIN

            RETRY:
            -- Limit the number of retries to avoid infinite loop
            IF @retry_count >= 50
                THROW 50000, 'Exceeded maximum retry attempts for generating unique Beneficiary IDs', 1;

            -- Generate random numbers
            SET @bene_cust_secondary_id = FORMAT(CAST(FLOOR(RAND() * (999999999 - 100000 + 1) + 100000) AS BIGINT), '0000000000');
            
            -- Check for uniqueness of customer secondary ID
            IF EXISTS (SELECT 1 FROM cust_info WHERE cust_secondary_id = @bene_cust_secondary_id)
            BEGIN
                SET @retry_count = @retry_count + 1;
                GOTO RETRY;
            END;

            -- Insert into acct_bene
            INSERT INTO acct_bene (acct_bene_id,
                                   acct_id,
                                   bene_cust_secondary_id,
                                   bene_first_name,
                                   bene_last_name,
                                   bene_tax_id,
                                   relationship_id,
                                   bene_portion)
            VALUES (@acct_bene_id,
                    @acct_id,
                    @bene_cust_secondary_id,
                    @bene_first_name,
                    @bene_last_name,
                    @bene_tax_id,
                    @relationship_id,
                    @bene_portion);
        END

        -- Conditionally insert into acct_poa
        IF (@acct_poa_id IS NOT NULL AND
            @acct_id IS NOT NULL AND
            @poa_cust_secondary_id IS NOT NULL AND
            @poa_first_name IS NOT NULL AND
            @poa_last_name IS NOT NULL AND
            @poa_tax_id IS NOT NULL AND
            @poa_id IS NOT NULL)
        
        BEGIN

            RETRY:
            -- Limit the number of retries to avoid infinite loop
            IF @retry_count >= 50
                THROW 50000, 'Exceeded maximum retry attempts for generating unique Power of Attorney IDs', 1;

            -- Generate random numbers
            SET @poa_cust_secondary_id = FORMAT(CAST(FLOOR(RAND() * (999999999 - 100000 + 1) + 100000) AS BIGINT), '0000000000');
            
            -- Check for uniqueness of customer secondary ID
            IF EXISTS (SELECT 1 FROM cust_info WHERE cust_secondary_id = @poa_cust_secondary_id)
            BEGIN
                SET @retry_count = @retry_count + 1;
                GOTO RETRY;
            END;

            -- Insert into acct_poa
            INSERT INTO acct_poa (acct_poa_id,
                                  acct_id,
                                  poa_cust_secondary_id,
                                  poa_first_name,
                                  poa_last_name,
                                  poa_tax_id,
                                  poa_id)
            VALUES (@acct_poa_id,
                    @acct_id,
                    @poa_cust_secondary_id,
                    @poa_first_name,
                    @poa_last_name,
                    @poa_tax_id,
                    @poa_id)
        END

        -- If code execution reaches this point, commit the transaction
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- An error occurred, rollback the transaction
        ROLLBACK TRANSACTION;

        -- Capture the error state
        SET @error_state = 1;

        -- Re-throw the error for further diagnosis or for client application to handle
        THROW;
    END CATCH;

    -- Return the error state (0 = success, 1 = failure)
    SELECT @error_state AS 'Error_state';
END;