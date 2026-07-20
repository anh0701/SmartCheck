from models.product import Product


class ProductRepository:

    @staticmethod
    def find_by_code(code):

        return Product.query.filter_by(
            code=code
        ).first()


    @staticmethod
    def find_by_id(product_id):

        return Product.query.get(product_id)