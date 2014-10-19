describe('login', function() {
    browser.ignoreSynchronization = true;
    browser.get('');

    it('should check correct title', function() {
        expect(browser.getTitle()).toBe('Test Automation with Protractor');
    });

});
