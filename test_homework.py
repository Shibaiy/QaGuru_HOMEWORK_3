
from selene import browser, have, be
import  pytest
from faker import Faker


def test_autarisation():
    fake = Faker('ru_RU')
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type(fake.first_name())
    browser.element('#lastName').should(be.blank).type(fake.last_name())
    browser.element('#userEmail').should(be.blank).type(fake.email())
    browser.element('[for="gender-radio-1"]').click()
    browser.driver.execute_script("window.scrollBy(0, 400)")
    browser.element('#userNumber').should(be.blank).type(fake.random_int(1000000000,9999999999))
    browser.element('#dateOfBirthInput').click()
    browser.element(f'//*[@class="react-datepicker__month-select"]/option[{fake.random_int(1,12)}]').click()
    browser.element(f'//*[@class="react-datepicker__year-select"]/option[{fake.random_int(1, 201)}]').click()
    browser.element(f"//*[@class='react-datepicker__month']/*[{fake.random_int(1,6)}]/*[{fake.random_int(1,7)}]").click()
    browser.element('#subjectsInput').should(be.blank).type('e')
    browser.element(f"//*[@id='react-select-2-option-{fake.random_int(0,5)}']").click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.driver.execute_script("window.scrollBy(0, 300)")
    browser.element('#currentAddress').should(be.blank).type(fake.address())
    browser.element('#state').click()
    browser.element(f'//*[@id="react-select-3-option-{fake.random_int(0,3)}"]').click()
    browser.element('#city').click()
    browser.element(f'//*[@id="react-select-4-option-{fake.random_int(0,1)}"]').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
