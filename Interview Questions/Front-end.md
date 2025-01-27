Here are ten **general front-end development** interview questions that a full-stack developer might encounter, along with detailed answers:

---

### 1. **What is the difference between `display: none`, `visibility: hidden`, and `opacity: 0`?**

**Answer:**

- **`display: none`:** Removes the element from the document flow. It is not rendered, and space is not reserved for it.
- **`visibility: hidden`:** Hides the element but keeps it in the document flow. Space is reserved, but the element is not visible.
- **`opacity: 0`:** Makes the element fully transparent but keeps it in the document flow. It remains interactive (e.g., clickable).

---

### 2. **Explain the CSS Box Model.**

**Answer:**
The CSS Box Model describes the structure of an element, consisting of:

- **Content:** The actual content (text, images, etc.).
- **Padding:** Space between the content and the border.
- **Border:** A line surrounding the padding and content.
- **Margin:** Space outside the border, separating the element from other elements.

The total width/height of an element is calculated as:

```
Total Width = width + padding-left + padding-right + border-left + border-right + margin-left + margin-right
```

---

### 3. **What are the differences between `let`, `const`, and `var` in JavaScript?**

**Answer:**

- **`var`:** Function-scoped. Can be redeclared and updated. Hoisted to the top of its scope.
- **`let`:** Block-scoped. Cannot be redeclared but can be updated. Not hoisted.
- **`const`:** Block-scoped. Cannot be redeclared or updated (for primitive values). Not hoisted.

Example:

```javascript
if (true) {
  var a = 1; // Function-scoped
  let b = 2; // Block-scoped
  const c = 3; // Block-scoped
}
console.log(a); // 1
console.log(b); // ReferenceError
console.log(c); // ReferenceError
```

---

### 4. **What is event delegation in JavaScript?**

**Answer:**
Event delegation is a technique where you attach a single event listener to a parent element to handle events for all its child elements. This is useful for dynamically added elements and improves performance by reducing the number of event listeners.

Example:

```javascript
document.getElementById("parent").addEventListener("click", (event) => {
  if (event.target.matches("button")) {
    console.log("Button clicked:", event.target.textContent);
  }
});
```

---

### 5. **What are the differences between `null`, `undefined`, and `undeclared` in JavaScript?**

**Answer:**

- **`null`:** An intentional absence of any value. It is an assignment value.
- **`undefined`:** A variable that has been declared but not assigned a value.
- **`undeclared`:** A variable that has not been declared using `var`, `let`, or `const`.

Example:

```javascript
let a; // undefined
let b = null; // null
console.log(c); // ReferenceError (undeclared)
```

---

### 6. **How does the `this` keyword work in JavaScript?**

**Answer:**
The `this` keyword refers to the context in which a function is executed. Its value depends on how the function is called:

- **Global context:** `this` refers to the `window` object (in browsers) or `global` object (in Node.js).
- **Object method:** `this` refers to the object the method belongs to.
- **Event listener:** `this` refers to the element that triggered the event.
- **Arrow functions:** `this` is lexically scoped (inherited from the parent scope).

Example:

```javascript
const obj = {
  name: "Alice",
  greet: function () {
    console.log("Hello, " + this.name);
  },
};
obj.greet(); // Hello, Alice
```

---

### 7. **What is the purpose of semantic HTML?**

**Answer:**
Semantic HTML uses meaningful tags (e.g., `<header>`, `<article>`, `<footer>`) to describe the structure and content of a webpage. Benefits include:

- Improved accessibility for screen readers.
- Better SEO (search engines understand the content better).
- Easier maintenance and readability for developers.

Example:

```html
<header>
  <h1>Website Title</h1>
  <nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
  </nav>
</header>
<main>
  <article>
    <h2>Article Title</h2>
    <p>Article content...</p>
  </article>
</main>
<footer>
  <p>Footer content</p>
</footer>
```

---

### 8. **What are the differences between `GET` and `POST` requests?**

**Answer:**

- **`GET`:**
  - Used to request data from a server.
  - Data is sent in the URL as query parameters.
  - Has a length limit and is less secure for sensitive data.
- **`POST`:**
  - Used to send data to a server (e.g., form submissions).
  - Data is sent in the request body.
  - No length limit and more secure for sensitive data.

---

### 9. **What is CORS, and how do you handle it?**

**Answer:**
CORS (Cross-Origin Resource Sharing) is a security feature that restricts cross-origin HTTP requests. It is enforced by browsers to prevent malicious websites from accessing resources on another domain.

**Handling CORS:**

- On the server, set the `Access-Control-Allow-Origin` header to allow specific origins or `*` for all origins.
- For development, use a proxy server or disable CORS in the browser (not recommended for production).

Example (Node.js/Express):

```javascript
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
  next();
});
```

---

### 10. **What are some ways to optimize front-end performance?**

**Answer:**

- **Minify and compress assets:** Reduce the size of CSS, JavaScript, and HTML files.
- **Lazy load images:** Load images only when they are visible in the viewport.
- **Use a CDN:** Serve static assets from a Content Delivery Network for faster delivery.
- **Reduce HTTP requests:** Combine files and use sprites for small images.
- **Enable caching:** Use browser caching and server-side caching.
- **Optimize critical rendering path:** Prioritize loading above-the-fold content.
- **Debounce and throttle events:** Reduce the frequency of expensive operations like resizing or scrolling.

---

### 11. **What the various ways to create an object in JavaScript?**

**Answer:**
In JavaScript, there are several ways to create an object, depending on your use case. Here are the most common methods:

### 1. **Object Literal Syntax** (Simplest Way)

```javascript
const person = {
  name: "Alice",
  age: 30,
  greet: function () {
    console.log(`Hi, I'm ${this.name}`);
  },
};
person.greet(); // Output: Hi, I'm Alice
```

### 2. **Using the `Object` Constructor**

```javascript
const person = new Object();
person.name = "Bob";
person.age = 25;
person.greet = function () {
  console.log(`Hi, I'm ${this.name}`);
};
person.greet(); // Output: Hi, I'm Bob
```

### 3. **Using a Constructor Function**

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Hi, I'm ${this.name}`);
  };
}
const person = new Person("Charlie", 28);
person.greet(); // Output: Hi, I'm Charlie
```

### 4. **Using ES6 Classes**

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  greet() {
    console.log(`Hi, I'm ${this.name}`);
  }
}
const person = new Person("Diana", 32);
person.greet(); // Output: Hi, I'm Diana
```

### 5. **Using `Object.create()`**

```javascript
const prototype = {
  greet() {
    console.log(`Hi, I'm ${this.name}`);
  },
};
const person = Object.create(prototype);
person.name = "Eve";
person.age = 27;
person.greet(); // Output: Hi, I'm Eve
```

### 6. **Using Factory Functions**

```javascript
function createPerson(name, age) {
  return {
    name,
    age,
    greet() {
      console.log(`Hi, I'm ${this.name}`);
    },
  };
}
const person = createPerson("Frank", 29);
person.greet(); // Output: Hi, I'm Frank
```

### 7. **Using JSON Syntax for Data**

If you're just transferring data (no methods), JSON is useful:

```javascript
const person = JSON.parse('{"name": "Grace", "age": 31}');
console.log(person.name); // Output: Grace
```

### Choose the Right Method

- For simple structures, use **object literals**.
- For reusability, use **classes** or **constructor functions**.
- For inheritance or prototypes, use **`Object.create()`**.
- For custom factories, use **factory functions**.
