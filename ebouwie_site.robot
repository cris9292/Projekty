*** Settings ***
Documentation  Projekt Zaliczeniowy Automatyzajca Testu z wykorzystaniem RobotFramework dla WSB Sprawdził:Adam Przybyła
Library    BuiltIn
Library    Selenium2Library
Suite Setup     Go to page
Suite Teardown    Close All Browsers

*** Variables ***
${PAGE}     https://www.eobuwie.com.pl/
${BROWSER}     chrome
${valid_name}     Krzysztof
${invalid_email}     123opwgmail.com
${valid_password}     Password123@!
${valid_surname}    Malolepszy
${expect_result}    Wprowadzono niepoprawny adres e-mail
*** Test Cases ***
Strona Ebuwie Przypadek testowy automatyzacja
    Twitter fill in a form
    Comparison

*** Keywords ***
Twitter fill in a form
    Click Element     xpath://*[@id="top"]/body/header/div[3]/div/div[2]/a[2]
    Input text     id:firstname   ${valid_name}           #imie
    Input text     id:lastname   ${valid_surname}           #nazwisko
    Input text     id:password   ${valid_password}              #haslo
    Input text     id:confirmation    ${valid_password}          #confirm hasla
    Input text     id:email_address    ${invalid_email}                  #email
    Click Element    xpath://*[@id="form-validate"]/label[2]/input

Comparison
    ${error_notice}     Get Text     xpath=//*[@id="form-validate"]/div[3]/span
    Should be equal     ${error_notice}     ${expect_result}
    log to console      ${error_notice}

Go to page
     Open Browser     ${PAGE}     ${BROWSER}
     Maximize Browser Window

