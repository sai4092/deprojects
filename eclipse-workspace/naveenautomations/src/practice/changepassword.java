package practice;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.annotations.Test;

public class changepassword {
	
	
	
	public void changepassword() {

		WebElement ele1 = launchbrowser.driver.findElement(By.linkText("Change your password"));
		ele1.click();
		
		WebElement ele2 = launchbrowser.driver.findElement(By.xpath("//*[@id=\"input-password\"]"));
		ele2.sendKeys("saibaba");
		
		WebElement ele3 = launchbrowser.driver.findElement(By.xpath("//*[@id=\"input-confirm\"]"));
		ele3.sendKeys("saibaba");
		
		
		WebElement ele4 = launchbrowser.driver.findElement(By.xpath("/html/body/div[2]/div/div/form/div/div[2]/input"));
		ele4.click();
		
		launchbrowser.driver.navigate().to("https://naveenautomationlabs.com/opencart/");
		

		WebElement ele5 = launchbrowser.driver.findElement(By.xpath("//*[@id=\"column-right\"]/div/a[13]"));
		ele5.click();
		

		
		
	
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
