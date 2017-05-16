$(function (){

$("#effects").validate({
	rules: {
		name:"required",
		dob:"required",
		// mobile:"required",
		// password:"required",
		cpassword:"required",

		Email: {
			required : true,
			email : true,
		},
		mobile:{
			maxlength:10,
			minlength:10,
		},
		password :{
			required:true,
			minlength:8,
			// equalTo: "#cpassword",
		},
		cpassword :{
			required:true,
			equalTo:"#password",
		}
	},
	messages: {
		name :"Your name is required!!",
		dob:"Your date of birth is required!!",
		mobile:{
			required:"Your phone number is required!!",
			maxlength: "Give ten digit mobile number!!",
			minlength: "Give ten digit mobile number!!",
		},
		Email:{
			required:"Your Email is required!!",

		},
		password:{
			required:"Choose a password!!",
			minlength:"Atleast 8 character required!!",
		},
		cpassword:{
			required:"This field is required!!",
			equalTo:"Password does not matches!!",
		},

	},

} );

});