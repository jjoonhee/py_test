from roboter.view import console
from roboter.model import ranking

DEFAULT_ROBOT_NAME = "Yeji"
DEFAULT_USER_NAME = "Joonhee"
DEFAULT_COLOR = "blue"


class Robot:
    """
    This is a base class will be inherited
    """

    def __init__(self, robot_name=DEFAULT_ROBOT_NAME, username=DEFAULT_USER_NAME, color=DEFAULT_COLOR):
        self.robot_name = robot_name
        self.username = username
        self.color = color

    def hello(self):
        while True:
            template = console.get_template_path("welcome.txt", self.color)
            username = input(template.substitute({"robot_name": self.robot_name}))

            if username:
                self.username = username.title()
                break


class RestaurantRobot(Robot):
    """
    This is a class to recommend restaurant
    """
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(robot_name= name)
        self.ranking_model = ranking.RankingModel()

    def _hello_decorator(func):
        def wrapper(self):
            if not self.username:
                self.hello()
            return func(self)
        return wrapper


    @_hello_decorator
    def recommend_restaurant(self):
        new_recommend_restaurant = self.ranking_model.get_most_popular()
        print(new_recommend_restaurant)
        if not new_recommend_restaurant:
            return None
        will_recommend_restaurants = [new_recommend_restaurant]

        while True:
            template = console.get_template_path("recommend_restaurant.txt", self.color)
            is_yes = input(template.substitute({
                "RESTAURANT_NAME":  new_recommend_restaurant
            }))

            if is_yes.lower() == "y" or is_yes.lower() == "yes":
                break

            if is_yes.lower() == "n" or is_yes.lower() == "no":
                new_recommend_restaurant = self.ranking_model.get_most_popular(
                    not_list=will_recommend_restaurants
                )
                if not new_recommend_restaurant:
                    break
                will_recommend_restaurants.append(new_recommend_restaurant)

    @_hello_decorator
    def ask_user_favorite(self):
        while True:
            template = console.get_template_path(
                "ask_restaurant.txt", self.color
            )
            restaurant = input(template.substitute({
                "user_name": self.username
            }))
            if restaurant:
                self.ranking_model.increment(restaurant)
                break

    @_hello_decorator
    def thank_you(self):
        """Show words of appreciation to users."""
        template = console.get_template_path('thanks.txt', self.color)
        print(template.substitute({'USER_NAME': self.username}))






