For a **Spring Boot** interview, being well-versed in **JUnit 5** and **Mockito** is essential for demonstrating your understanding of **unit testing** and **mocking**. Here’s what you should focus on:

---

### 📋 **1. JUnit 5 Basics**

- **Annotations:**  
  | Annotation | Description |
  |----------------------|---------------------------------------------------------|
  | `@Test` | Marks a method as a test case. |
  | `@BeforeEach` | Runs before each test method. |
  | `@AfterEach` | Runs after each test method. |
  | `@BeforeAll` | Runs once before all tests (`static`). |
  | `@AfterAll` | Runs once after all tests (`static`). |
  | `@Disabled` | Disables a test method or class. |
  | `@Nested` | Groups related tests together. |
  | `@DisplayName` | Custom name for test methods. |
  | `@ParameterizedTest` | Runs tests with multiple values. |

- **Assertions (from `org.junit.jupiter.api.Assertions`):**
  ```java
  assertEquals(expected, actual);
  assertTrue(condition);
  assertFalse(condition);
  assertThrows(Exception.class, () -> methodCall());
  assertAll("grouped assertions",
      () -> assertEquals(4, 2 + 2),
      () -> assertTrue("spring".startsWith("s"))
  );
  ```

---

### 🧪 **2. Mockito Essentials**

- **Mocking Dependencies:**

  ```java
  @Mock
  private UserRepository userRepository;

  @InjectMocks
  private UserService userService;
  ```

- **Common Annotations:**  
  | Annotation | Purpose |
  |-----------------|--------------------------------------------------------|
  | `@Mock` | Creates a mock instance. |
  | `@InjectMocks` | Injects mocks into the tested object. |
  | `@Spy` | Partial mock – real methods are called unless stubbed. |
  | `@Captor` | Captures method arguments. |

- **Mocking Behavior:**

  ```java
  when(userRepository.findById(1L)).thenReturn(Optional.of(new User("John")));
  doThrow(new RuntimeException()).when(userRepository).deleteById(2L);
  ```

- **Verifying Interactions:**

  ```java
  verify(userRepository, times(1)).save(any(User.class));
  verify(userRepository, never()).deleteById(1L);
  ```

- **Argument Captor:**

  ```java
  @Captor
  ArgumentCaptor<User> userCaptor;

  verify(userRepository).save(userCaptor.capture());
  assertEquals("John", userCaptor.getValue().getName());
  ```

---

### ⚙️ **3. Testing Spring Boot Components**

- **With `@SpringBootTest` (Integration Testing):**

  ```java
  @SpringBootTest
  class UserServiceIntegrationTest {

      @Autowired
      private UserService userService;

      @Test
      void shouldCreateUser() {
          User user = userService.createUser("Jane");
          assertNotNull(user.getId());
      }
  }
  ```

- **With `@WebMvcTest` (Controller Testing):**

  ```java
  @WebMvcTest(UserController.class)
  class UserControllerTest {

      @Autowired
      private MockMvc mockMvc;

      @MockBean
      private UserService userService;

      @Test
      void shouldReturnUser() throws Exception {
          when(userService.getUser(1L)).thenReturn(new User("John"));

          mockMvc.perform(get("/users/1"))
              .andExpect(status().isOk())
              .andExpect(jsonPath("$.name").value("John"));
      }
  }
  ```

- **With `@DataJpaTest` (Repository Testing):**

  ```java
  @DataJpaTest
  class UserRepositoryTest {

      @Autowired
      private UserRepository userRepository;

      @Test
      void shouldSaveUser() {
          User user = new User("Anna");
          User savedUser = userRepository.save(user);
          assertNotNull(savedUser.getId());
      }
  }
  ```

---

### 🚀 **4. Mocking Strategies**

- **`when().thenReturn()` vs. `doReturn().when()`**

  - Use `when().thenReturn()` for non-void methods.
  - Use `doReturn().when()` for spying or avoiding method execution.

- **Mocking Void Methods:**
  ```java
  doNothing().when(userRepository).deleteById(anyLong());
  doThrow(new IllegalArgumentException()).when(userRepository).deleteById(999L);
  ```

---

### 🛠 **5. Advanced Mockito Techniques**

- **Using `doAnswer()` for Complex Logic:**

  ```java
  doAnswer(invocation -> {
      Long id = invocation.getArgument(0);
      return new User("User" + id);
  }).when(userRepository).findById(anyLong());
  ```

- **Mocking Private Methods (With PowerMock or Reflection):**  
  _Note: Mention only if asked; it's generally discouraged._

---

### 💡 **6. Common Interview Questions**

1. **"How do you mock dependencies in Spring Boot tests?"**  
   _Answer: Using `@Mock` and `@InjectMocks` for unit tests or `@MockBean` for Spring-managed beans._

2. **"What's the difference between `@Mock` and `@Spy`?"**  
   _Answer: `@Mock` creates a dummy object; `@Spy` allows partial mocking, calling real methods unless stubbed._

3. **"How would you test a Controller in isolation?"**  
   _Answer: Use `@WebMvcTest` with `MockMvc` to mock HTTP requests and responses._

4. **"How do you handle testing asynchronous methods?"**  
   _Answer: Use `CompletableFuture`, `CountDownLatch`, or `awaitility` library to wait for async execution._

5. **"How would you mock a static method?"**  
   _Answer: With **Mockito 3.4+** using `mockStatic()`, or with **PowerMock** for older versions._
   ```java
   try (MockedStatic<UtilityClass> mocked = mockStatic(UtilityClass.class)) {
       mocked.when(() -> UtilityClass.staticMethod()).thenReturn("Mocked");
       assertEquals("Mocked", UtilityClass.staticMethod());
   }
   ```

---
