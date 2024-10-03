import { ApolloClient, InMemoryCache, HttpLink, ApolloProvider } from '@apollo/client';

// Setting up the HTTP link instance to connect to your GraphQL endpoint
const httpLink = new HttpLink({
  uri: '/graphql',  // This will work correctly due to the proxy setup in package.json
});

// Creating the Apollo Client instance
const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
});

export default client;
