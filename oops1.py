class employee:
    def __init__(self):
        self.id=123
        self.salary=3000
        self.designation="SDE"
    def travel(self,dest):
        print(f"emplo travelling to {dest}")
sam=employee()
sam.travel("hyd")
# print(sam.id)
