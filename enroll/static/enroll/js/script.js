

// Modal open function

function openModal(){
    console.log("click hua")
    // document.querySelector('.overlay').classList.add('overlayactive')
    document.querySelector('.subform').classList.add('active')
    console.log("modal chal raha hai")

}


// Modal close function
function  closeModal() {
    // document.querySelector('.overlay').classList.remove('overlayactive');
    document.querySelector('.subform').classList.remove('active');
  }; 



  var ip=document.querySelectorAll('input');

  for(let i=0;i<ip.length;i++)
  {
    sub1=ip[i];
  }

// var form=document.querySelector('.container form');
// var submitBtn=document.querySelector('.btn-submitform');

// submitBtn.addEventListener('click',function(e){

//     var inputs=form.querySelectorAll('input');


//     for(var i=0;i<inputs.length;i++){
//         if(inputs[i].value.trim()==''){

//             e.preventDefault();
//             alert("Please fill in all fields");
//             return ;
//         }


//         if(/\d/.test(inputs[i].value)){
//             e.preventDefault();
//             alert("Grades cannot contain numbers");
//             return;
//         }

//         if (/[^A-E+\s]/i.test(inputs[i].value)) {
//             e.preventDefault(); // Prevent the form from being submitted
//             alert('Grades can only contain the letters A, B, C, D, E, +, and whitespace.');
//             return;
//           }

//         }
//         form.submit()
//     });



    const form2 = document.getElementById('my-form');
    form2.addEventListener('submit', (event) => {
      event.preventDefault(); // prevent the default form submission behavior
      const formData = new FormData(form2); // create a new FormData object from the form inputs
      const formValues = Object.fromEntries(formData); // convert the FormData object to a plain JavaScript object
      console.log(formValues); // log the form values to the console (or do something else with them)
    });
   


