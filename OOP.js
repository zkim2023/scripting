// Define a simple class called Greeting
class Greeting {
    constructor(name) {
        this.name = name;
    }

    // Method to return a greeting message
    sayHello() {
        return 'Hello, ${this.name}! Welcome to our website.';
    }
}

// Create an instance of the Greeting class
const greeting = new Greeting("Alice");

// Display the greeting message in the element with id "output"
document.getElementByld("output").innerText = greeting.sayHello();