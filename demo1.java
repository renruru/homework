import java.io.File;

import org.openqa.selenium.By;
import org.openqa.selenium.By.ById;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.Assert;


public class demo1 {
	WebDriver driver;
	Actions action;
	
	demo1 (){
		this.driver = new ChromeDriver();
		this.action =new Actions(driver);
	}

	
	public void login(String[] users, String[] pwd) throws InterruptedException{
		driver.get("http://pawork.lenovo.com/oa/");
		driver.manage().window().maximize();
		WebElement userName = driver.findElement(ById.id("userName"));
		userName.sendKeys(users);
		WebElement passWord = driver.findElement(ById.id("password"));
		passWord.sendKeys(pwd);
		WebElement logIn = driver.findElement(ById.id("login"));
		logIn.click();
		Thread.sleep(3000);
	}
	
	public void writeRiBao() throws InterruptedException{
		driver.findElement(By.cssSelector("div >aside>section>ul>li:nth-child(5) >a>span ")).click();
		Thread.sleep(3000);
		WebElement ribaodengji = driver.findElement(By.cssSelector("body>div>aside>section>ul>li:nth-child(5)>ul>li:nth-child(2)"));
		Thread.sleep(3000);
		action.moveToElement(ribaodengji).click().perform();
	    WebElement ribaoVoew = driver.findElement(By.cssSelector("body > div > div.content-wrapper > section.content-header > h1"));
		Assert.assertEquals(ribaoVoew.isDisplayed(), true);
	}
	
	public static void main(String[] args) throws InterruptedException {
		//System.setProperty("", "");
//		File fire_chrome = new File(".\\tools\\chromedriver.exe");
		//System.setProperty("webdriver.chrome.driver", fire_chrome.getAbsolutePath());
		
		demo1 d = new demo1();
		d.login(new String[]{"renruru"},new String[]{"201515"});
		Thread.sleep(10000);
		d.writeRiBao();
		d.driver.quit();

	}

}
