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
	
	var page = $("#start");
	var txtUsername = $("#start").find("#username");
	var txtPassword = $("#start").find("#password");
	var btnLogin = $("#start").find("#login");
	
	self.initialize = function() {
		btnLogin.click(self.btnLoginClicked);
	};
	
	self.btnLoginClicked = function(event) {
		event.preventDefault();
		
		if (self.validateLogin()) {
			self.login();
		}
	};
	
	self.validateLogin = function() {
		var valid = true;
		if (txtUsername.val().length == 0) {
			txtUsername.css("border-color", "#f00");
			valid = false;
		} else {
			txtUsername.css("border-color", "");
		}
			
		if (txtPassword.val().length == 0) {
			txtPassword.css("border-color", "#f00");
			valid = false;
		} else {
			txtPassword.css("border-color", "");
		}
		
		return valid;
	};
	
	self.login = function() {
		$.mobile.changePage($("#dashboard"));
	};
};