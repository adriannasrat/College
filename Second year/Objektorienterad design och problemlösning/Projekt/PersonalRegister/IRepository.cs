using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PJU
{
	public interface IRepository<T>
	{
		Task AddAsync(T item);
		Task UpdateAsync(T item);
		Task DeleteAsync(string id);
		T GetById(string id);
		Dictionary<string, T> GetAll();
	}
}
