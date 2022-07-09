package practice;

import java.util.concurrent.TimeUnit;

public class home {

	public static void main(String[] args) {
		
		launchbrowser objlaunch = new launchbrowser();
		userregistration objregister =new userregistration();
		login objlogin = new login();
		changepassword objchangepassword = new changepassword();
		
		
		objlaunch.launchapplication();
		objregister.userregister();
		objlogin.loginuser();
		objchangepassword.changepassword();
		
		
		
		
		
		
		
		
		
		
		

	}

}
