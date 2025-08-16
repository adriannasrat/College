using System;
using System.ComponentModel;
using System.Text.Json.Serialization;

namespace PJU
{
	public class Bee
	{
		public string Id { get; set; }
		//[JsonConverter(typeof(DateTimeConverter))]
		public DateTime BirthDate { get; set; }
		[JsonIgnore]
		public bool HasWings { get; set; }
		private const int LifeSpanInDays = 21; // Bees live longer than ants.
		private static readonly Random _random = new Random();
		public Bee(DateTime birthDate)
		{
			BirthDate = birthDate;
			HasWings = true;
			Id = GenerateUniqueId();
		}
		public static Bee CreateWithRandomBirthDate(DateTime currentDate)
		{
			int randomDaysAgo = _random.Next(1, 22); // Random number between 1 and 21 days ago
			DateTime birthDate = currentDate.AddDays(-randomDaysAgo);
			return new Bee(birthDate);
		}

		private string GenerateUniqueId()
		{
			return Guid.NewGuid().ToString("N");
		}

		public bool IsAlive(DateTime currentDate)
		{
			return (currentDate - BirthDate).TotalDays <= LifeSpanInDays;
		}

		public override string ToString()
		{
			return $"ID: {Id}, Wings: {HasWings}";
		}

		public string ToString(DateTime currentDate)
		{
			return $"ID: {Id}, Alive: {IsAlive(currentDate)}, Wings: {HasWings}";
		}
	}
}
