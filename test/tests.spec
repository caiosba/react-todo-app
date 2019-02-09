require 'selenium-webdriver'

context "tests" do
  before :all do
    @wait = Selenium::WebDriver::Wait.new(timeout: 10)
  end
  
  before :each do |example|
    @driver = Selenium::WebDriver.for(:remote, url: 'http://localhost:9516')
  end

  it "should open the front page" do
    # expect(@driver.find_element(:css, '.task__required').text == '*').to be(true)
    # expect(@driver.page_source.include?('newteamwidetag')).to be(false)
    # @driver.action.send_keys(:enter).perform
    @driver.navigate.to('http://localhost:8080')
    expect(@driver.page_source.include?('Create your first todo! :)')).to be(true)
  end
end
