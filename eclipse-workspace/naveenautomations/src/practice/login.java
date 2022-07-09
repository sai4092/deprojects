package practice;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class login {
	
	public void loginuser() {
		WebElement ele = launchbrowser.driver.findElement(By.xpath("/html/body/nav/div/div[2]/ul/li[2]/a/span[1]"));		
		ele.click();
		
		WebElement ele1 = launchbrowser.driver.findElement(By.linkText("Login"));
		ele1.click();
		
		
		WebElement ele2 = launchbrowser.driver.findElement(By.xpath("//*[@id=\"input-email\"]"));		
		ele2.sendKeys("jastisaikumar20@gmail.com");
		
		
		WebElement ele3 = launchbrowser.driver.findElement(By.xpath("//*[@id=\"input-password\"]"));		
		ele3.sendKeys("Saibaba");
		
		
		WebElement ele4 = launchbrowser.driver.findElement(By.xpath("/html/body/div[2]/div/div/div/div[2]/div/form/input"));
		
		
		ele4.click();
		
		

		
	
		
		
	
		
	}
	

}
