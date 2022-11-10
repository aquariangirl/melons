"""Classes for melon orders."""
class AbstractMelonOrder:
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax 

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        
        if self.species == "Christmas":
            base_price = base_price * 1.5

        if self.order_type == "international" and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price
            total += 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, tax = 0.08, order_type = 'domestic')
 

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, tax = 0.17, order_type = 'international')
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """An order from the US Government"""
    def __init__(self, species, qty, passed_inspection):

        super().__init__(species, qty, tax = 0.0, 
                            order_type = "Government")
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

        return self.passed_inspection
    """Takes a Boolean input, passed, and updates whether or not 
    the melon has passed inspection. """
    
    
    
