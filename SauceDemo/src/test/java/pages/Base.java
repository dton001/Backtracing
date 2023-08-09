package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Base {
	public WebDriver driver;
    protected Properties properties;
	
	public Base(WebDriver driver){
        this.driver = driver;
        readProperty();
	}

    public void readProperty(){
        try (InputStream input = new FileInputStream(System.getProperty("user.dir") + "//src//test//resources//Info.properties")) {
            Properties prop = new Properties();
            prop.load(input);
            this.properties = prop;
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
	
    public void click(By by){
        driver.findElement(by).click();
    }

    public void sendText(By by, String s) {
    	driver.findElement(by).sendKeys(s);
    }
}
