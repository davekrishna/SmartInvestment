window.addEventListener("scroll",function(){
    let navbar=document.getElementById("menu")
    if(window.pageYOffset>500){
      navbar.classList.remove('bg-transparent')
      navbar.classList.add('scrolled')
    }
    else{
      navbar.classList.remove('scrolled')
      navbar.classList.add('bg-transparent')
    }
  })