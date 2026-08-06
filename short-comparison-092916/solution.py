// REST
fetch('/users/1')
fetch('/users/1/posts')

// GraphQL
query {
  user(id: 1) { name posts { title } }
}
