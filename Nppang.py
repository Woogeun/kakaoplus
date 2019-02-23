
######################### User class
class User:
	def __init__(self, name=""):
		self.name = name
		self.income = 0
		self.outcome = 0
		pass

	def set_income(self, income):
		outcome = self.get_outcome()
		if income < 0:
			self.income += income
		elif income >= outcome:
			self.income += income - outcome
			self.outcome = 0
		else:
			self.income = 0
			self.outcome = outcome - income

	def set_outcome(self, outcome):
		income = self.get_income()
		if outcome < 0:
			self.outcome += outcome
		elif outcome >= income:
			self.outcome += outcome - income
			self.income = 0
		else:
			self.outcome = 0
			self.income = income - outcome

	def get_name(self):
		return self.name

	def get_income(self):
		return self.income

	def get_outcome(self):
		return self.outcome



############################ debug functions
def print_user(user):
	print("{:>5} : +{:>8}, -{:>8}".format(user.get_name(), user.get_income(), user.get_outcome()))


def print_users(users):
	print("="*10 + "users list" + "="*10)
	for user in users:
		print_user(user)
	print("="*10 + "="*10 + "="*10)


def check_validation(debug=False):
	summation = 0
	for user in all_users:
		summation += user.get_income()
		summation -= user.get_outcome()


	if debug:
		print_users(all_users)

	assert(summation == 0)


def check_allzero():
	for user in all_users:
		assert(user.get_income() == 0)
		assert(user.get_outcome() == 0)


##################### basic Nppang function
def dist_won(paied_user, will_pay_users, amount):
	check_validation()

	assert(paied_user not in will_pay_users)

	num_of_users = len(will_pay_users) + 1
	share = amount / num_of_users

	paied_user.set_income(share * (num_of_users - 1))
	for user in will_pay_users:
		user.set_outcome(share)

	check_validation()


##################### minimal transfer algorithm
def minimal_transfer_algorithm():
	sorted_users = sorted(all_users, key=lambda user: -user.get_outcome())
	print_users(sorted_users)

	idx_out = 0
	idx_in = len(sorted_users) - 1

	process_string = "=" * 10 + "minimal transfer algorithm" + "=" * 10 + "\n"

	while(idx_out < idx_in):

		amount = 0

		out_user = sorted_users[idx_out]
		in_user = sorted_users[idx_in]

		outcome = out_user.get_outcome()
		income = in_user.get_income()

		if outcome == income:
			out_user.set_outcome(-outcome)
			in_user.set_income(-income)
			idx_out += 1
			idx_in -= 1
			amount = outcome
			pass
		elif outcome > income:
			out_user.set_outcome(-income)
			in_user.set_income(-income)
			idx_in -= 1
			amount = income
			pass
		else:
			out_user.set_outcome(-outcome)
			in_user.set_income(-outcome)
			idx_out += 1
			amount = outcome
			pass


		process_string += "{:>5} --> {:>5} : {:>8} won\n".format(out_user.get_name(), in_user.get_name(), amount)
		# print(process_string)
		# print_users(sorted_users)
		check_validation()

	process_string += "="*46
	print(process_string)

	check_allzero()







## test code
if __name__ == "__main__":
	u1 = User("u1")
	u2 = User("u2")
	u3 = User("u3")
	u4 = User("u4")
	all_users = [u1, u2, u3, u4]


	dist_won(u1, [u2, u3, u4], 2000)
	dist_won(u2, [u3, u4], 3000)
	dist_won(u3, [u4], 1000)
	dist_won(u4, [u1, u3], 6000)

	minimal_transfer_algorithm()
