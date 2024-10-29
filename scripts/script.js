let currentIndex = 0;
// Use querySelectorAll to get all elements with the class 'gallery-slide'
const slides = Array.from(document.querySelectorAll('.gallery-slide'));
const totalSlides = slides.length;

// Check if there are no slides and handle it appropriately
if (totalSlides === 0) {
    console.error('No slides found'); 
    
} else {
    function showNextSlide() {
        // Hide all slides first
        slides.forEach(slide => {
            slide.style.display = 'none';
        });

        // update current index
        currentIndex = (currentIndex + 1) % totalSlides;

        // Show the next slide
        slides[currentIndex].style.display = 'block';
    }

    // Show the first slide initially
    slides.forEach((slide, index) => {
        slide.style.display = index === 0 ? 'block' : 'none';
    });

    // Change slide every 3 seconds
    setInterval(showNextSlide, 4000);
}

//Get all accordion headers
let accordionHeader = document.querySelectorAll('.accordion-header');

//Loop through the headers to add click event
accordionHeader.forEach(header => {
    header.addEventListener('click', () => {

        //Get the corresponding content
        const content = header.nextElementSibling;

        //Toggle thhe active class on content
        content.classList.toggle('active');

        
    });
});

