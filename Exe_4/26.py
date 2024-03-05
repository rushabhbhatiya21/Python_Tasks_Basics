class Sample:
    x, y = 10, 10

    def __init__(self, sample1=0, sample2=0, sample3=0, sample4=0):
        self.sample1 = sample1
        self.sample2 = sample2
        self.sample3 = sample3
        self.sample4 = sample4

    def get_all_attributes(self):
        global_variables = globals()
        local_variables = locals()

        print("Global Attribute:", global_variables.get("global_attribute"))
        print("Local Attribute:", local_variables.get("local_attribute"))


sample = Sample()
sample.get_all_attributes()