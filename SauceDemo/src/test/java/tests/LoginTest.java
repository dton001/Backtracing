package tests;

import org.testng.annotations.Test;
import pages.LoginPage;
import org.testng.annotations.BeforeMethod;

public class LoginTest extends BaseTest{
	LoginPage loginPage;

    @BeforeMethod
	private void setup(){
        super.setUp();
        loginPage = new LoginPage(this.driver);
    }

    @Test
    public void login(){
        loginPage.login();
    }
}