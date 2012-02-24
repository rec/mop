var ApplicationController = function() {
	var self = this;
	
	this.currentUser = new User();
};

var User = function() {
	var self = this;
	
	this.userState = UserState.NONE;
	this.bidAskState = BidAskState.NONE;
	this.negotiationState = NegotiationState.NONE;
	this.paymentState = PaymentState.NONE;
	
	this.loggedIn = false;
};

//Initialize application pages
window.addEventListener('load', function () {
		document.addEventListener('deviceready', function () {
				alert("PhoneGap is now loaded!");
		}, false);
}, false);

$("#start").live("pageinit", function(event) {
	if (Application.currentUser.userState === UserState.LOGGED_IN)
		$.mobile.changePage("#dashboard");

	var controller = new StartController();
	controller.initializeView();
});

$("#dashboard").live("pageinit", function(event) {
	if (Application.currentUser.userState !== UserState.LOGGED_IN)
		$.mobile.changePage("#start");
	});

$("#map").live("pageinit", function(event) {
	if (Application.currentUser.userState !== UserState.LOGGED_IN)
		$.mobile.changePage("#start");
	
	var controller = new MapController();
	controller.initializeView();
});

//Controller to handle the startup page
var StartController = function() {
	var self = this;
	
	self.page = $("#start");
	self.txtUsername = $("#start").find("#username");
	self.txtPassword = $("#start").find("#password");
	self.btnLogin = $("#start").find("#login");
	
	this.initializeView = function() {
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
		if (self.txtUsername.val().length === 0) {
			self.txtUsername.css("border-color", "#f00");
			valid = false;
		} else {
			self.txtUsername.css("border-color", "");
		}
			
		if (self.txtPassword.val().length === 0) {
			self.txtPassword.css("border-color", "#f00");
			valid = false;
		} else {
			self.txtPassword.css("border-color", "");
		}
		
		return valid;
	};
	
	self.login = function() {
		//TODO: Authenticate with server
		Application.currentUser.userState = UserState.LOGGED_IN;
		$.mobile.changePage($("#dashboard"));
	};
};

var MapController = function() {
	var self = this;
	this.mapCanvas = $("#map").find("#map-canvas");
	
	this.initializeView = function() {
		this.mapCanvas.gmap();
		
		if (typeof phonegap !== "undefined") {
			navigator.geolocation.getCurrentPosition(self.centerMap, function(error) { }); 
		}
	};
	
	this.centerMap = function(position) {
		var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
		this.mapCanvas.gmap({"center": pos});
	};
};

var UserState = {
	NONE: {value: 0, name: "No State"},
	LOGGED_IN: {value: 1, name: "Logged In"},
	FAILURE_LOGIN: {value: 2, name: "Invalid Username/Password"},
	FAILURE_NAME: {value: 3, name: "No Name Exists"},
	FAILURE_NETWORK: {value: 4, name: "No Network Connectivity"},
	FAILURE_SERVER: {value: 5, name: "Server Is Unreachable"},
	FAILURE_ERROR: {value: 6, name: "Server Error"}
};

var BidAskState = {
	NONE: {value: 0, name: "No Offer"},
	BID: {value: 1, name: "User Offering To Buy Parking Space"},
	ASK: {value: 2, name: "User Offering To Sell Parking Space"}
};

var NegotiationState = {
	NONE: {value: 0, name: "No Negotiation"},
	LOCATING: {value: 1, name: "User Is Setting Location For Offer"},
	SETTING: {value: 2, name: "Location Set, Setting Price/Time"},
	WAITING: {value: 3, name: "User Initiated Offer, No Replies"},
	NEGOTIATING: {value: 4, name: "Tentatively Accepted Offer, Negotiating Terms"},
	AGREEMENT: {value: 5, name: "User And Other Party Agreed To Match Bid/Ask"},
	DELIVERED: {value: 6, name: "User Delivered, Other Party Has Not Yet"}
};

var PaymentState = {
	NONE: {value: 0, name: "No Payment"},
	PAYMENT: {value: 0, name: "Payment"}
};

var Application = new ApplicationController();