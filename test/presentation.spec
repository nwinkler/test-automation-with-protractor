describe('login', function() {
    browser.ignoreSynchronization = true;
    browser.get('');

    it('should check correct title', function() {
        expect(browser.getTitle()).toBe('Test Automation with Protractor');
    });

    it('should find the H1 in the page', function() {
        var present = element(by.css('.present'));

        var h1 = present.element(by.css('h1'));

        expect(h1.getText()).toBe('TEST AUTOMATION WITH PROTRACTOR');
    });
});
