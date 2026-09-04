# Software Design Principles

## KISS - Keep It Simple, Stupid
** Priority**: HIGH
**Guideline**: Eliminate code duplication
**Implementation**: Extract repeated logic into reusable functions/modules
**Exception**: Don't violate KISS to follow DRY - some duplication is better than forced abstraction.

Avoid unnecessary complexity. The simplest solution is often the best.

```javascript
// ❌ Over-engineered
class UserNameFormatter {
  constructor(user) { this.user = user }
  format() { return `${this.user.firstName} ${this.user.lastName}` }
}
const name = new UserNameFormatter(user).format()

// ✅ Simple
const name = `${user.firstName} ${user.lastName}`
```

## DRY - Don't Repeat Yourself
**Priority**: HIGH
**Guideline**: Eliminate code duplication
**Implementation**: Extract repeated logic into reusable functions/modules
**Exception**: Don't violate KISS to follow DRY - some duplication is better than forced abstraction

Every piece of knowledge should have a single, authoritative representation.

```javascript
// ❌ Repeated logic
function validateEmail(email) { return email.includes('@') }
function checkUserEmail(email) { return email.includes('@') }

// ✅ Single source of truth
function isValidEmail(email) { return email.includes('@') }
```

## YAGNI - You Aren't Gonna Need It
**Priority**: HIGH
**Guideline**: Build only what's needed now
**Implementation**: Resist adding features "just in case" - add them when requirements demand it
**Exception**: Core architecture decisions that are costly to change later (database schema, API contracts)

Don't add functionality until it's actually needed.

```javascript
// ❌ Building for hypothetical future needs
class User {
  constructor(name) {
    this.name = name
    this.permissions = []      // "might need later"
    this.preferences = {}      // "might need later"
    this.socialConnections = [] // "might need later"
  }
}

// ✅ Only what's needed now
class User {
  constructor(name) {
    this.name = name
  }
}
```

## SOLID Principles

### S - Single Responsibility
**Priority**: HIGH
**Guideline**: One class/function = one job
**Implementation**: If you describe a class with "and", split it
**Exception**: Small utility classes or scripts where splitting adds unnecessary complexity

A class should have only one reason to change.

```javascript
// ❌ Multiple responsibilities
class User {
  save() { /* database logic */ }
  sendEmail() { /* email logic */ }
  generateReport() { /* PDF logic */ }
}

// ✅ Single responsibility each
class User { /* user data only */ }
class UserRepository { save(user) { } }
class EmailService { send(to, message) { } }
```

### O - Open/Closed
**Priority**: MEDIUM
**Guideline**: Add new behavior without changing existing code
**Implementation**: Use composition, strategies, or plugin patterns
**Exception**: Simple scripts or prototypes where flexibility isn't needed

Open for extension, closed for modification.

```javascript
// ❌ Requires modifying existing code
function calculateDiscount(type, price) {
  if (type === 'student') return price * 0.2
  if (type === 'senior') return price * 0.3
  // Must edit this function for each new type
}

// ✅ Extend without modifying
const discounts = {
  student: price => price * 0.2,
  senior: price => price * 0.3
}
// Add new types by extending the object
discounts.employee = price => price * 0.25
```

### L - Liskov Substitution
**Priority**: MEDIUM
**Guideline**: Subclasses must honor parent class contracts
**Implementation**: If overriding changes behavior unexpectedly, reconsider the inheritance
**Exception**: Rarely violated intentionally - usually indicates a design flaw

Subtypes must be substitutable for their base types.

```javascript
// ❌ Square breaks Rectangle's contract
class Rectangle {
  setWidth(w) { this.width = w }
  setHeight(h) { this.height = h }
}
class Square extends Rectangle {
  setWidth(w) { this.width = this.height = w } // Surprise!
}

// ✅ Separate classes or common interface
class Shape { getArea() { } }
class Rectangle extends Shape { /* width × height */ }
class Square extends Shape { /* side × side */ }
```

### I - Interface Segregation
**Priority**: MEDIUM
**Guideline**: Many small interfaces beat one large interface
**Implementation**: Split fat interfaces into focused ones
**Exception**: Simple applications where interface granularity adds overhead

Clients shouldn't depend on interfaces they don't use.

```javascript
// ❌ Fat interface
class Worker {
  work() { }
  eat() { }
  sleep() { }
}

// ✅ Segregated interfaces
class Workable { work() { } }
class Eatable { eat() { } }
// Combine only what's needed
```

### D - Dependency Inversion
**Priority**: HIGH
**Guideline**: High-level modules shouldn't depend on low-level details
**Implementation**: Inject dependencies, use interfaces/abstractions
**Exception**: Leaf nodes (UI components, simple utilities) can depend on concrete implementations

Depend on abstractions, not concrete implementations.

```javascript
// ❌ Direct dependency on implementation
class OrderService {
  constructor() {
    this.db = new MySQLDatabase() // Locked to MySQL
  }
}

// ✅ Depend on abstraction
class OrderService {
  constructor(database) {
    this.db = database // Any database works
  }
}
```

## Rule of Three
**Priority**: MEDIUM
**Guideline**: Wait for the third occurrence before abstracting
**Implementation**: First time: write it. Second time: note it. Third time: refactor it
**Exception**: Obviously reusable utilities (formatters, validators) can be extracted earlier

Refactor when you see the same pattern three times.

```javascript
// First time: just write it
// Second time: note the duplication
// Third time: refactor!

// ❌ After third occurrence, still duplicated
formatUserName(user)
formatAdminName(admin)
formatGuestName(guest)

// ✅ Refactor on third occurrence
formatName(person)
```

## Separation of Concerns
**Priority**: HIGH
**Guideline**: Each module handles one aspect (UI, data, logic, etc.)
**Implementation**: Split by responsibility - presentation, business logic, data access
**Exception**: Very small scripts or single-purpose tools where splitting adds complexity

Different concerns should be in different modules.

```javascript
// ❌ Mixed concerns
function handleSubmit() {
  const data = document.getElementById('form').value  // UI
  if (!data.email.includes('@')) return               // Validation
  fetch('/api/users', { body: data })                 // Network
  document.getElementById('msg').innerText = 'Saved'  // UI
}

// ✅ Separated concerns
const ui = { getFormData() { }, showMessage(msg) { } }
const validate = { email(e) { return e.includes('@') } }
const api = { saveUser(data) { } }

function handleSubmit() {
  const data = ui.getFormData()
  if (!validate.email(data.email)) return
  api.saveUser(data)
  ui.showMessage('Saved')
}
```

## Composition Over Inheritance
**Priority**: HIGH
**Guideline**: Build complex objects by combining simple ones
**Implementation**: Use mixins, delegation, or dependency injection instead of deep hierarchies
**Exception**: True "is-a" relationships with stable hierarchies (e.g., Error types)

Favor object composition over class inheritance.

```javascript
// ❌ Deep inheritance hierarchy
class Animal { }
class Mammal extends Animal { }
class Dog extends Mammal { }
class SwimmingDog extends Dog { } // What about flying dogs?

// ✅ Compose behaviors
const canSwim = { swim() { console.log('Swimming') } }
const canBark = { bark() { console.log('Woof!') } }

function createDog(name) {
  return { name, ...canBark }
}

function createSwimmingDog(name) {
  return { name, ...canBark, ...canSwim }
}
```

## Law of Demeter
**Priority**: MEDIUM
**Guideline**: Only call methods on objects you directly own or receive
**Implementation**: Use delegation or create wrapper methods instead of chaining
**Exception**: Fluent APIs and builders are designed for chaining - this is acceptable

Only talk to your immediate friends. Don't reach through objects.

```javascript
// ❌ Reaching through objects (train wreck)
const street = order.getCustomer().getAddress().getStreet()

// ✅ Ask, don't reach
const street = order.getDeliveryStreet()

// Or use delegation
class Order {
  getDeliveryStreet() {
    return this.customer.getDeliveryStreet()
  }
}
```

---

## Conflicts & Trade-offs

These principles can conflict with each other. Here's how to navigate the tensions:

### DRY vs KISS
**Conflict:** Eliminating duplication can lead to complex abstractions.
```javascript
// ❌ DRY-obsessed: One generic function for everything
function processEntity(entity, type, options = {}) {
  const config = configs[type]
  return config.transform(entity, options)
}

// ✅ KISS-friendly: Some duplication, but clear
function processUser(user) { return { ...user, fullName: `${user.first} ${user.last}` } }
function processOrder(order) { return { ...order, total: order.items.sum() } }
```
**Resolution:** Keep duplication if the abstraction is harder to understand than the original.

### DRY vs YAGNI
**Conflict:** DRY encourages extracting common code early, YAGNI says "wait until you need it".
**Resolution:** Follow **Rule of Three** – wait for the third occurrence before abstracting.

### SOLID vs KISS
**Conflict:** Full SOLID implementation can be over-engineering for simple projects.
```javascript
// ❌ Full SOLID for a simple Todo-app = overkill
// 15 classes, 8 interfaces, dependency injection framework...

// ✅ KISS: One file, 50 lines, works
```
**Resolution:** SOLID pays off in larger systems. For small projects, choose KISS.

### Open/Closed vs YAGNI
**Conflict:** O/C says "build for future extension", YAGNI says "don't build for hypothetical needs".
**Resolution:** Make code *easy to change*, but don't build in flexibility you don't know you need.

---

## Complementary Principles

These principles work well together:

- **KISS + YAGNI** → Both prevent over-engineering
- **SRP + Separation of Concerns** → Same idea at different levels (class vs module)
- **DRY + Rule of Three** → Rule of Three tells you *when* to apply DRY
- **Composition + Dependency Inversion** → Both promote loosely coupled, flexible code
- **Liskov + Interface Segregation** → Both ensure healthy contracts

---

## Priority Guide for AI Agents

When principles conflict, follow this priority order:

1. **KISS** – When in doubt, choose the simpler solution
2. **YAGNI** – Don't build for problems you don't have
3. **Separation of Concerns** – Keep things apart
4. **DRY** – But not at any cost
5. **SOLID** – Apply gradually as the system grows

### Decision Tree
```
Is the solution simple and readable?
├── No → Simplify (KISS)
└── Yes → Does it solve a real, current problem?
    ├── No → Remove it (YAGNI)
    └── Yes → Is there duplication?
        ├── Less than 3 occurrences → Leave it (Rule of Three)
        └── 3+ occurrences → Can you extract without adding complexity?
            ├── No → Keep duplication (KISS > DRY)
            └── Yes → Extract (DRY)
```

---

## Summary

When writing code:
1. Start simple (KISS, YAGNI)
2. Don't repeat yourself (DRY, Rule of Three)
3. Keep things focused (Single Responsibility, Separation of Concerns)
4. Design for flexibility (Open/Closed, Composition over Inheritance)
5. Minimize coupling (Law of Demeter, Dependency Inversion)

**Remember:** These are guidelines, not laws. Context determines which principle takes precedence.
