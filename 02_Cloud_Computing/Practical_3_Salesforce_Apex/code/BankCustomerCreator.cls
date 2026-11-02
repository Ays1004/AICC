// ============================================================
// Cloud Computing Practical 3 - Bank application (Visualforce)
// Class name: BankCustomerCreator
//
// This is the controller for BankCustomerForm.page.
// Create this Apex class, then create the Visualforce page with
// the same name used in the "extensions" attribute.
// ============================================================

public class BankCustomerCreator {

    public String customerName { get; set; }
    public String contactNumber { get; set; }
    public String customerSegment { get; set; }
    public String accountNumber { get; set; }
    public String accountType { get; set; }

    public List<SelectOption> segmentOptions { get; set; }
    public List<SelectOption> accountTypeOptions { get; set; }

    public BankCustomerCreator(ApexPages.StandardController controller) {
        segmentOptions = new List<SelectOption>();
        segmentOptions.add(new SelectOption('', '- None -'));
        segmentOptions.add(new SelectOption('Retail Banking', 'Retail Banking'));
        segmentOptions.add(new SelectOption('Corporate Banking', 'Corporate Banking'));
        segmentOptions.add(new SelectOption('Private Banking', 'Private Banking'));
        segmentOptions.add(new SelectOption('Investment Banking', 'Investment Banking'));

        accountTypeOptions = new List<SelectOption>();
        accountTypeOptions.add(new SelectOption('', '- None -'));
        accountTypeOptions.add(new SelectOption('Savings', 'Savings'));
        accountTypeOptions.add(new SelectOption('Current', 'Current'));
    }

    public PageReference createCustomer() {
        System.debug('Creating new bank customer');

        if (!String.isEmpty(customerName)) {
            // Note: the standard Account.Type picklist does not contain
            // Savings/Current by default, so the segment and account type
            // are stored in Description. This keeps the demo working
            // without changing Salesforce's standard picklist.
            Account customer = new Account(
                Name = customerName,
                Phone = contactNumber,
                AccountNumber = accountNumber,
                Description = 'Segment: ' + customerSegment +
                              '; Account Type: ' + accountType
            );

            insert customer;

            PageReference pg = new PageReference('/' + customer.Id);
            pg.setRedirect(true);
            return pg;
        } else {
            ApexPages.addMessage(
                new ApexPages.Message(
                    ApexPages.Severity.ERROR,
                    'Please enter Customer Name'
                )
            );
        }

        return null;
    }

    public PageReference cancelCreation() {
        return new PageReference(
            '/' + Schema.SObjectType.Account.getKeyPrefix() + '/o'
        );
    }
}
