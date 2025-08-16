using PersonalRegister;

namespace PJU
{
	public class AntFactory : IPersonalFactory<Ant>
	{
		public Ant Create(DateTime currentDate)
		{
			return Ant.CreateWithRandomBirthDate(currentDate); // Generate ants with a birthdate in the past
		}
	}
}
