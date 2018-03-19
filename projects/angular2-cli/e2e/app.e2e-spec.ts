import { Angular2CliPage } from './app.po';

describe('angular2-cli App', function() {
  let page: Angular2CliPage;

  beforeEach(() => {
    page = new Angular2CliPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
