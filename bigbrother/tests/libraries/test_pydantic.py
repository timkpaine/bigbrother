from pydantic import BaseModel, Field
from ..common import create_tester


class MySubModel(BaseModel):
    x: list = []
    y: dict = {}


class MyOtherSubModel(BaseModel):
    x: list = Field(default_factory=list)
    y: dict = Field(default={})


class MyModel(BaseModel):
    a: MySubModel
    b: MyOtherSubModel
    c: MyOtherSubModel = Field(default_factory=MyOtherSubModel)
    d: MySubModel = Field(default=MySubModel())
    e: list = []


class TestPydantic:
    def test_pydantic_setattr(self):
        my_sub_model = MySubModel()
        my_other_sub_model = MyOtherSubModel()
        x = MyModel(a=my_sub_model, b=my_other_sub_model)

        x, called = create_tester(
            x,
            "setitem",
            (
                "d",
                my_sub_model,
            ),
            {},
        )
        x.d = my_sub_model

        assert called[0]
        assert x.d == my_sub_model

    def test_pydantic_setattr_sub(self):
        my_sub_model = MySubModel()
        my_other_sub_model = MyOtherSubModel()
        x = MyModel(a=my_sub_model, b=my_other_sub_model)
        x.d, called = create_tester(x.d, "setitem", ("x", [1]), {})
        x.d.x = [1]

        assert called[0]
        assert x.d.x == [1]
