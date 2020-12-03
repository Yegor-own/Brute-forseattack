import strategies
import generators
import queries

strategies.DumbStrategy(
    login_generator = generators.LoginGenerator(),
    password_generator = generators.PopularStringGenerator(),
    query = queries.try_local_server
).run()