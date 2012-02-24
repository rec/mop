//Initialize application pages

$("#start").live("pageinit", function(event) {
	var controller = new StartController();
	controller.initialize();
});

$("#dashboard").live("pageinit", function(event) {
	
});

//Controller to handle the startup page
var StartController = function() {
	var self = this;
	
	self.page = $("#start");
	self.txtUsername = $("#start").find("#username");
	self.txtPassword = $("#start").find("#password");
	self.btnLogin = $("#start").find("#login");
	
	self.initialize = function() {
		self.btnLogin.click(self.btnLoginClicked);
	};
	
	self.btnLoginClicked = function(event) {
		event.preventDefault();
		
		if (self.validateLogin()) {
			self.login();
		}
	};
	
	self.validateLogin = function() {
		var valid = true;
		if (self.txtUsername.val().length == 0) {
			self.txtUsername.css("border-color", "#f00");
			valid = false;
		} else {
			self.txtUsername.css("border-color", "");
		}
			
		if (self.txtPassword.val().length == 0) {
			self.txtPassword.css("border-color", "#f00");
			valid = false;
		} else {
			self.txtPassword.css("border-color", "");
		}
		
		return valid;
	};
	
	self.login = function() {
		$.mobile.changePage($("#dashboard"));
	};
};