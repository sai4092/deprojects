package practice;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.Test;

public class launchbrowser {
	public static WebDriver driver;
	
	
	public void launchapplication() {
		System.setProperty("webdriver.gecko.driver","C:\\selenium\\geckodriver.exe");
		 driver = new FirefoxDriver();
		driver.navigate().to("https://naveenautomationlabs.com/opencart/");
		driver.manage().window().maximize();
		}

}
