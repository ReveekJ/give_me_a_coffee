def is_pydantic(obj: object):
    """ Checks whether an object is pydantic. """
    return type(obj).__class__.__name__ == "ModelMetaclass"


def model_to_entity(schema):
    """
        Iterates through pydantic schema and parses nested schemas
        to a dictionary containing SQLAlchemy models.
        Only works if nested schemas have specified the Meta.orm_model.
    """
    if is_pydantic(schema):
        try:
            converted_model = model_to_entity(dict(schema))
            return schema.Meta.orm_model(**converted_model)

        except AttributeError:
            model_name = schema.__class__.__name__
            raise AttributeError(f"Failed converting pydantic model: {model_name}.Meta.orm_model not specified.")

    elif isinstance(schema, list):
        return [model_to_entity(model) for model in schema]

    elif isinstance(schema, dict):
        for key, model in schema.items():
            schema[key] = model_to_entity(model)

    return schema
