using PersonalRegister;
using PJU;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PersonalRegister
{
	public class BeeFactory : IPersonalFactory<Bee>
	{
		public Bee Create(DateTime currentDate)
		{
			return Bee.CreateWithRandomBirthDate(currentDate);
		}
	}
}
