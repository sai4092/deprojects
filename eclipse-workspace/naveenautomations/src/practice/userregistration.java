package practice;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class userregistration {
	
	public void userregister() {
		
		
		WebElement ele = launchbrowser.driver.findElement(By.xpath("/html/body/nav/div/div[2]/ul/li[2]/a/span[1]"));		
		ele.click();
		WebElement ele1 = launchbrowser.driver.findElement(By.linkText("Register"));
		ele1.click();
		WebElement ele2 = launchbrowser.driver.findElement(By.id("input-firstname"));
		ele2.sendKeys("sai");
		
		WebElement ele3 = launchbrowser.driver.findElement(By.id("input-lastname"));
		ele3.sendKeys("jastisai");
		
		
		WebElement ele4 = launchbrowser.driver.findElement(By.xpath("//*[@id=\"input-email\"]"));
		ele4.sendKeys("jastisaikumar20@gmail.com");
		
		WebElement ele5 = launchbrowser.driver.findElement(By.id("input-telephone"));
		ele5.sendKeys("9676245585");	
		
		WebElement ele6 = launchbrowser.driver.findElement(By.id("input-password"));
		ele6.sendKeys("Saibaba");
		
		
		WebElement ele7 = launchbrowser.driver.findElement(By.id("input-confirm"));
		ele7.sendKeys("Saibaba");
		
		WebElement ele8 = launchbrowser.driver.findElement(By.xpath("/html/body/div[2]/div/div/form/fieldset[3]/div/div/label[2]/input"));
		ele8.click();
		

		WebElement ele9 = launchbrowser.driver.findElement(By.xpath("/html/body/div[2]/div/div/form/div/div/input[1]"));
		ele9.click();
		

		WebElement ele10 = launchbrowser.driver.findElement(By.xpath("/html/body/div[2]/div/div/form/div/div/input[2]"));
		ele10.click();
		
		
	
		
	
		
		
		
		
		
		
	
		
		
		
	


		
		
		
		
		
		
	}
	

}
