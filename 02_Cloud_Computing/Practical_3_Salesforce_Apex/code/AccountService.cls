// ============================================================
// Cloud Computing Practical 3 - Salesforce Apex
// Class name: AccountService
//
// HOW TO USE:
// Developer Console -> File -> New -> Apex Class
// Name: AccountService
// Delete the default code, paste this file, press Ctrl+S.
// Then press Ctrl+E (Execute Anonymous) and paste execute_anonymous.apex.
// ============================================================

public class AccountService {

    // Simple version: create an Account with only the Name field.
    public static void createAccount(String accountName) {
        Account newAccount = new Account();
        newAccount.Name = accountName;

        try {
            insert newAccount;
            System.debug('Account created with Id: ' + newAccount.Id);
        } catch (DmlException e) {
            System.debug('Error creating account: ' + e.getMessage());
        }
    }

    // Version with more fields.
    // industry must be a valid Account Industry picklist value,
    // for example: Banking, Finance, Technology, Healthcare.
    public static void createAccountWithDetails(
        String accountName,
        String phone,
        String industry,
        String accountNumber
    ) {
        Account newAccount = new Account();
        newAccount.Name = accountName;
        newAccount.Phone = phone;
        newAccount.Industry = industry;
        newAccount.AccountNumber = accountNumber;

        try {
            insert newAccount;
            System.debug('Account created with Id: ' + newAccount.Id);
        } catch (DmlException e) {
            System.debug('Error creating account: ' + e.getMessage());
        }
    }

    // Delete an Account by its Salesforce Id.
    // The Id is the 15- or 18-character value in the account URL.
    public static void deleteAccount(Id accountId) {
        if (accountId == null) {
            System.debug('Account Id cannot be null');
            return;
        }

        try {
            Account acc = [SELECT Id FROM Account WHERE Id = :accountId LIMIT 1];
            delete acc;
            System.debug('Account with Id ' + accountId + ' has been deleted.');
        } catch (QueryException e) {
            System.debug('Error finding account: ' + e.getMessage());
        } catch (DmlException e) {
            System.debug('Error deleting account: ' + e.getMessage());
        }
    }
}
