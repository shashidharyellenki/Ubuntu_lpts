const FirstName = document.querySelector('#FirstName');
const LastName = document.querySelector('#LastName');
const Email = document.querySelector('#Email');
const Username = document.querySelector('#Username');
const Password = document.querySelector('#Password');
const Confrim_Password = document.querySelector('#Confrim_Password');
const Birthday_date = document.querySelector('#Birthday_date');
const phone = document.querySelector('#phone');
const Register = document.getElementById('Register')
const validateEmail =/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
let components = [FirstName, LastName, Email, Username, Password, Confrim_Password, Birthday_date, phone];
//adding eventlistners to all the components
// testing
console.log(FirstName.parentElement.children)



Register.disabled = true;
components.forEach(component=>{
   component.addEventListener('input',()=>{
       let id_span = component.parentElement.children[2];
       if(component.value === "" ){
           id_span.innerHTML="feild can't be empty";
        }else{
            id_span.textContent="";
        }
        if((FirstName.value !=""   && LastName.value !="" ) && (Email.value !=""  && Username.value  !="") &&( Password.value   !="" && Confrim_Password.value !="" )   && (Birthday_date.value  !=""  && phone.value  !="" ) ){
            Register.disabled=false
        } 
        
        if(component == Password){
            console.log(Password.value)
            if(Password.value.length >= 8){
                id_span.innerHTML="strength: good";
                id_span.classList.add('green');
                id_span.classList.remove('blue');
            }else if (Password.value.length == 5){
                id_span.innerHTML="strength: Moderate";
                id_span.classList.add('blue');
            }
        }
    })
})
//using date class
const date = new Date();
//extracing year from complete date to check age
const year = date.getFullYear(); //2022


//validating input fields

Register.addEventListener('click',()=>{
    //validating passwords
    if(Password.value !== Confrim_Password.value){
        Register.disabled=true;
        alert("password and confrimpassword is not match")
    }
    //validating email
    if(!validateEmail.test(Email.value)){
        Register.disabled=true;
        alert("Invalid Email")
    }
    //validating phone number
    if(phone.value.length != 10){
        Register.disabled=true;
        alert("Invalid Phone Number")
    }
    //validating date
    if((year-userYear)<13){
        Register.disabled=true;
        alert("Minimum age is 13 and your are too young for this course");
    }
    //noticing user
    if((Password.value === Confrim_Password.value) && (validateEmail.test(Email.value)) && (phone.value.length === 10) && ((year-userYear)>=13)){
        alert("Hey form submitted sucessfully!!");
    }
    
})




/**
 * 
 * else{
        alert("Hey form submitted sucessfully!!");
    }
 * 
 */