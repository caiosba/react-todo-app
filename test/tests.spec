require 'selenium-webdriver'

context "tests" do
  before :all do
    @wait = Selenium::WebDriver::Wait.new(timeout: 10)
  end

  before :each do |example|
    @driver = Selenium::WebDriver.for(:remote, url: 'http://localhost:9516')
  end

  it "should open the frontpage with an empty list" do
    @driver.navigate.to('http://localhost:8080')
    expect(@driver.page_source.include?('No TODOs found')).to be(true)
  end
  
  it "should add a task" do
    @driver.navigate.to('http://localhost:8080')
    task = 'Ir ao mercado'
    expect(@driver.page_source.include?(task)).to be(false)
    @driver.find_element(:css, 'input').click
    @driver.action.send_keys(task).perform
    @driver.action.send_keys(:enter).perform
    sleep 1
    expect(@driver.page_source.include?(task)).to be(true)
  end
end
