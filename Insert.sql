USE [BankDB]
GO
/****** Object:  StoredProcedure [dbo].[InsertCustInfo]    Script Date: 9/27/2023 6:42:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[InsertCustInfo]
    -- Parameters for cust_info
    @first_name nvarchar(200),
    @middle_name nvarchar(200) = NULL,
    @last_name nvarchar(200),
    @suffix varchar(3) = NULL,
    @date_of_birth date,
    @client_since date = NULL,

	-- Parameters for cust_contact
    @cust_email nvarchar(200),
    @cust_phone_home varchar(15),
    @cust_phone_business varchar(15) = NULL,
    @cust_address varchar(200),
    @cust_address_2 varchar(200) = NULL,
    @cust_city varchar(85),
    @cust_state varchar(2),
    @cust_zip varchar(10),
    @cust_country smallint,

	-- Parameters for cust_emp
    @employment_status bit,
    @employer_name varchar(200),
    @occupation varchar(500),

	-- Parameters for cust_id
    @id_type tinyint,
    @id_state varchar(2),
    @id_num varchar(25),
    @id_exp varchar(25),
    @mothers_maiden nvarchar(200),

    -- Parameters for cust_privacy
    @voice_auth bit = 0,
    @do_not_call bit = 0,
    @share_affiliates bit = 0,

    -- Parameters for cust_tax
    @cust_tax_id varchar(25)

AS
BEGIN
    SET NOCOUNT ON;
	-- Declare variables
    DECLARE @retry_count int = 0; -- Retry counter for data generation
    DECLARE @cust_secondary_id varchar(10);
    DECLARE @cust_id int;
	DECLARE @state_id tinyint;
	DECLARE @zip_id int;
	DECLARE @result_state_id tinyint;
	DECLARE @result_zip_id int;
	DECLARE @id_state_id tinyint;
	DECLARE @result_id_state tinyint;

    BEGIN TRANSACTION; -- Start a new transaction
    
    BEGIN TRY
        RETRY_CUST_INFO:
			-- Get retry count and compare to max amount
            IF @retry_count >= 100
                THROW 50000, 'Exceeded maximum retry attempts for generating unique Cust IDs', 1;

			-- Generate cust_secondary_id - Format as 0000000000 with prevailing zeroes
            SET @cust_secondary_id = FORMAT(CAST(FLOOR(RAND() * (999999999 - 100000 + 1) + 100000) AS BIGINT), '0000000000');

			-- Check to see if cust_secondary_id is already taken
            IF EXISTS (SELECT 1 FROM cust_info WHERE cust_secondary_id = @cust_secondary_id)
            BEGIN
                SET @retry_count = @retry_count + 1;
                GOTO RETRY_CUST_INFO;
            END

			-- Get today's date for client_since
            IF @client_since IS NULL
                SET @client_since = CAST(GETDATE() AS DATE);

            -- Pre-validation check for cust_info
            IF (@cust_secondary_id IS NULL OR
                @first_name IS NULL OR
                @last_name IS NULL OR
                @date_of_birth IS NULL OR
                @client_since IS NULL)
            BEGIN
                RAISERROR('Missing required cust_info parameters', 16, 1);
                ROLLBACK TRANSACTION; -- Rollback transaction if parameters are missing
                RETURN;
            END

			-- Insert into cust_info
            INSERT INTO cust_info 
                (cust_secondary_id,
                 first_name,
                 middle_name,
                 last_name,
                 suffix,
                 date_of_birth,
                 client_since)
            VALUES
                (@cust_secondary_id,
                 @first_name,
                 @middle_name,
                 @last_name,
                 @suffix,
                 @date_of_birth,
                 @client_since);

            SET @cust_id = SCOPE_IDENTITY();
			
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
                RAISERROR('Missing required cust_contact parameters', 16, 1);
                ROLLBACK TRANSACTION; -- Rollback transaction if parameters are missing
                RETURN;
            END
			
			-- Select state_id from LU_state where match is found and set as tinyint
			SELECT @state_id = state_id FROM LU_state WHERE state_abbr = @cust_state;
			SET @result_state_id = CAST(@state_id AS tinyint);
			
			-- Select sip_id from LU_zip where match is found and set as int
			SELECT @zip_id = zip_id FROM LU_zip WHERE zip = @cust_zip;
			SET @result_zip_id = CAST(@zip_id as int);

			-- Insert into cust_contact
			INSERT INTO cust_contact
				(cust_id,
				 cust_email,
				 cust_phone_home,
				 cust_phone_business,
				 cust_address,
				 cust_address_2,
				 cust_city,
				 cust_state,
				 cust_zip,
				 cust_country)
			VALUES
				(@cust_id,
				 @cust_email,
				 @cust_phone_home,
				 @cust_phone_business,
				 @cust_address,
				 @cust_address_2,
				 @cust_city,
				 @result_state_id,
				 @result_zip_id,
				 @cust_country);
			
			-- Pre-validation check for cust_contact
			IF (@employment_status IS NULL OR
				@employer_name IS NULL OR
				@occupation IS NULL)
			BEGIN
                RAISERROR('Missing required cust_contact parameters', 16, 1);
                ROLLBACK TRANSACTION; -- Rollback transaction if parameters are missing
                RETURN;
            END	
			
			-- Insert into cust_emp
			INSERT INTO cust_emp 
				(cust_id,
				 employment_status,
				 employer_name,
				 occupation)
			VALUES
				(@cust_id,
				 @employment_status,
				 @employer_name,
				 @occupation);

			-- Pre-validation check for cust_id
			IF (@id_type IS NULL OR
				@id_state IS NULL OR
				@id_num IS NULL OR
				@id_exp IS NULL OR
				@mothers_maiden IS NULL)
			BEGIN
                RAISERROR('Missing required cust_id parameters', 16, 1);
                ROLLBACK TRANSACTION; -- Rollback transaction if parameters are missing
                RETURN;
            END	

			-- Select state_id from LU_state where match is found and set as tinyint
			SELECT @id_state_id = state_id FROM LU_state WHERE state_abbr = @id_state;
			SET @result_id_state = CAST(@state_id AS tinyint);

			-- Insert into cust_id
			INSERT INTO cust_id
				(cust_id,
				 id_type,
				 id_state,
				 id_num,
				 id_exp,
				 mothers_maiden)
			VALUES
				(@cust_id,
				 @id_type,
				 @result_state_id,
				 @id_num,
				 @id_exp,
				 @mothers_maiden);
			
			-- Insert into cust_privacy
			INSERT INTO cust_privacy 
				(cust_id,
				 voice_auth,
				 do_not_call,
				 share_affiliates)
			VALUES 
				(@cust_id,
				 @voice_auth,
				 @do_not_call,
				 @share_affiliates);

			-- Pre-validation check for cust_tax
			IF (@cust_tax_id IS NULL)
			BEGIN
                RAISERROR('Missing required cust_tax parameters', 16, 1);
                ROLLBACK TRANSACTION; -- Rollback transaction if parameters are missing
                RETURN;
            END	

			-- Insert into cust_tax
			INSERT INTO cust_tax
				(cust_id,
				 cust_tax_id)
			VALUES 
				(@cust_id,
				 @cust_tax_id);

            COMMIT TRANSACTION; -- Commit transaction if all operations succeed
    END TRY
    BEGIN CATCH
    ROLLBACK TRANSACTION; -- Rollback the transaction
		DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
		DECLARE @ErrorNumber INT = ERROR_NUMBER();
		DECLARE @ErrorLine INT = ERROR_LINE();
		DECLARE @ErrorProcedure NVARCHAR(200) = ISNULL(ERROR_PROCEDURE(), '-');

		RAISERROR('An error occurred while inserting data into cust_info. Error Number: %d, Error Line: %d, Error Procedure: %s, Error Message: %s', 
				  16, -- Severity
				  1,  -- State
				  @ErrorNumber, @ErrorLine, @ErrorProcedure, @ErrorMessage);
	END CATCH
END;