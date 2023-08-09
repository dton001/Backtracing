package pages;

import com.google.common.base.Equivalence;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.util.Base64;

public class LoginPage extends Base{
    public LoginPage(WebDriver driver){
        super(driver);
    }
    
    By usernameInput = By.xpath("//*[@id='user-name']");
    By passwordInput = By.xpath("//*[@id='password']");
    By loginButton = By.xpath("//*[@id='login-button']");

    public String encryptPassword(){
        Base64.Encoder encoder = Base64.getMimeEncoder();
        return new String(encoder.encodeToString(properties.getProperty("password").getBytes()));
    }
    public String decryptPassword(){
        Base64.Decoder decoder = Base64.getMimeDecoder();
        return new String(decoder.decode(properties.getProperty("password").getBytes()));
    }

    public void login(){
    	sendText(usernameInput, properties.getProperty("username"));
    	sendText(passwordInput, decryptPassword());
        click(loginButton);
    }
}
