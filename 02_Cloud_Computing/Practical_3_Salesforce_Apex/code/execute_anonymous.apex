// Paste this into: Developer Console -> Ctrl+E (Execute Anonymous) -> Execute
// The AccountService class must already be saved.

AccountService.createAccount('Test-1');
AccountService.createAccount('Test-2');

AccountService.createAccountWithDetails(
    'Rahul Sharma',
    '9876543210',
    'Banking',
    'ACC-1001'
);

// To delete an account:
// 1. Open the Accounts tab.
// 2. Click the account you created.
// 3. Copy the 15/18-character Id from the browser URL.
// 4. Uncomment the next line, paste the Id, and execute.
//
// AccountService.deleteAccount('001XXXXXXXXXXXXXXX');
