import itertools

class node:
	def __init__(self, nums, parent=None):
		self.nums = nums
		self.parent = parent
		self.children_cache = None

		self.subops = [leaf, addition, multiplication,subtraction]

	def children(self):
		if self.children_cache is None:
			self.children_cache = self.compute_children()
		return self.children_cache

	def compute_children(self):
		result = []
		for op in self.subops:
			op_obj = op(self.nums)
			if op_obj.is_valid():
				result.append((op_obj))
		return result

	def is_valid(self):
		return len(self.nums) >= 1

	def print(self):
		result = []
		for x in self.children():
			result += x.print()
		return result

	def value(self):
		result = set()
		for x in self.children():
			result |= x.value()
		return result


class leaf(node):
	def __init__(self, nums, parent=None):
		node.__init__(self, nums, parent=parent)
		self.subops = []

	def compute_children(self):
		return []

	def print(self):
		result = []
		for x in self.value():
			result.append(str(x))
		return result

	def value(self):
		result = set()
		for perm in itertools.permutations(self.nums):
			val = 0
			for digit in perm:
				val = 10*val + digit
			result.add(val)
		return result

	def symbol(self):
		return "#"


class binop(node):
	def __init__(self, nums, parent=None):
		node.__init__(self, nums, parent=parent)

	def is_valid(self):
		return len(self.nums) >= 2

	def value(self):
		result = set()
		for op1_obj,op2_obj in self.children():
			for op1 in op1_obj.value():
				for op2 in op2_obj.value():
					result.add(self.action(op1,op2))
		return result

	def print(self):
		result = []
		for op1_obj,op2_obj in self.children():
			for op1 in op1_obj.print():
				for op2 in op2_obj.print():
					ex = op1+self.symbol()+op2
					if self.use_paren():
						ex = '('+ex+')'
					result.append(ex)
		return result

	def compute_children(self):
		result = []
		for right_size in range(1,len(self.nums)): 
			for right_comb in itertools.combinations(self.nums, right_size):
				left_comb = set(self.nums) - set(right_comb)
				for op1 in self.subops:
					op1_obj = op1(left_comb, parent=self)
					if not op1_obj.is_valid():
						continue
					for op2 in self.subops:
						op2_obj = op2(right_comb, parent=self)
						if not op2_obj.is_valid():
							continue
						result.append((op1_obj,op2_obj))
		return result


class commutative(binop):
	def __init__(self, nums, parent=None):
		binop.__init__(self, nums, parent=parent)
	
	def compute_children(self):
		result = []
		# fix to discard commutative isos
		left_fix = next(iter(self.nums))
		right_options = set(self.nums) - {left_fix}
		# send to each side
		for right_size in range(1,len(right_options)+1): 
			for right_comb in itertools.combinations(right_options, right_size):
				left_comb = set(self.nums) - set(right_comb)
				for op1 in self.subops:
					op1_obj = op1(left_comb, parent=self)
					if not op1_obj.is_valid():
						continue
					for op2 in self.subops:
						op2_obj = op2(right_comb, parent=self)
						if not op2_obj.is_valid():
							continue
						#print(op1_obj.min(),left_comb, op2_obj.min(),right_comb)
						result.append((op1_obj,op2_obj))
		return result
				

class addition(commutative):
	def __init__(self, nums, parent=None):
		commutative.__init__(self, nums, parent=parent)

	def symbol(self):
		return "+"
	def use_paren(self):
		return type(self.parent) not in [addition, type(None)]
	def action(self, l, r):
		return l+r

class multiplication(commutative):
	def __init__(self, nums, parent=None):
		commutative.__init__(self, nums, parent=parent)

	def symbol(self):
		return "*"	
	def use_paren(self):
		return type(self.parent) not in [addition, subtraction, multiplication, type(None)]
	def action(self, l,r):
		return l*r

class subtraction(binop):
	def __init__(self, nums, parent=None):
		binop.__init__(self, nums, parent=parent)

	def symbol(self):
		return "-"	
	def use_paren(self):
		return type(self.parent) not in [addition, type(None)]
	def action(self, l,r):
		return l-r


if __name__ == "__main__":
	expr = node([4,4,4,4])
	print(expr.print())
	v = expr.value()
	v = list(v)
	v.sort()
	print(v)