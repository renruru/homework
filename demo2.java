import org.openqa.selenium.By;
import org.openqa.selenium.By.ByLinkText;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.Assert;


public class demo2 {

	/**
	 * @param args
	 */
	WebDriver driver =  new ChromeDriver();
	Actions action = new Actions(driver);
	
	
	WebElement name = driver.findElement(By.id("name"));
	WebElement content = driver.findElement(By.xpath("//*[@id='create_topic_form']/fieldset/div/div/div[2]/div[6]/div[1]/div/div/div/div[3]/pre"));
	WebElement add_reply = driver.findElement(By.cssSelector("#content > div:nth-child(2) > div.header > span"));
	WebElement contentView = driver.findElement(By.cssSelector("#reply_form>div>div>div.CodeMirror.cm-s-paper>div.CodeMirror-scroll>div.CodeMirror-sizer>div>div>div>div.CodeMirror-code>pre"));
	WebElement replyBtn = driver.findElement(By.cssSelector("#reply_form > div > div > div.editor_buttons > input"));
	WebElement deleteBtn = driver.findElement(By.cssSelector("#manage_topic > a.delete_topic_btn > i"));
	
	//	登录
	public boolean login(){
		driver.get("http://118.31.19.120:3000/");
		driver.manage().window().maximize();
		driver.findElement(ByLinkText.linkText("登录")).click();
		Assert.assertTrue(name.isDisplayed());
		name.sendKeys(new String[]{"testuser15"});
		driver.findElement(By.id("pass")).sendKeys(new String[]{"123456"});
		driver.findElement(By.id("pass")).submit();
		return true;	
	}
	
	//	发帖子
	public void post() throws InterruptedException{
		driver.findElement(By.xpath("//*[@id='create_topic_btn']/span")).click();
		driver.findElement(By.id("tab-value")).click();
		driver.findElement(By.cssSelector("#tab-value > option:nth-child(3)")).click();
		action.moveToElement(driver.findElement(By.id("title"))).click().sendKeys(new String[]{"今天不上班"}).perform();
		action.moveToElement(content).click().sendKeys(new String[]{"6666666666666"}).perform();
		driver.findElement(By.xpath("//*[@id='create_topic_form']/fieldset/div/div/div[4]/input")).click();
		Thread.sleep(3000);
	}
	
	//	回复帖子
	public void Reply() throws InterruptedException{
		System.out.println("add reply exits============"+add_reply);
		Assert.assertTrue(add_reply.isDisplayed());
		action.moveToElement(contentView).click().sendKeys(new String[]{"回复你的消息"}).perform();
		replyBtn.click();
		Thread.sleep(3000);
	}
	
	//	删除帖子
	public void delete() throws InterruptedException{
		deleteBtn.click();
		Thread.sleep(2000);
		driver.switchTo().alert().accept();
		Thread.sleep(3000);
	}

	public static void main(String[] args) throws Throwable {
		// TODO 自动生成的方法存根
		demo2 d = new demo2();
		d.login();
		d.post();
		d.Reply();
		d.driver.quit();
	}
}
