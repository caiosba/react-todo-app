require 'selenium-webdriver'

context "tests" do
  before :all do
    @wait = Selenium::WebDriver::Wait.new(timeout: 10)
  end

  before :each do |example|
    @driver = Selenium::WebDriver.for(:remote, url: 'http://localhost:9516')
  end
end
