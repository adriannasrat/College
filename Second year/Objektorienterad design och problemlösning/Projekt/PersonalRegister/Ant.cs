using System;
using System.ComponentModel;
using System.Text.Json.Serialization;

namespace PJU
{
	public class Ant
	{
		public string Id { get; set; }
		//[JsonConverter(typeof(DateTimeConverter))]
		public DateTime BirthDate { get; set; }
		public bool HasSafetyShoes { get; set; }
		private const int LifeSpanInDays = 14;
		private static readonly Random _random = new Random();

		// Constructor with explicit birthdate
		public Ant(DateTime birthDate)
		{
			BirthDate = birthDate;
			HasSafetyShoes = true;
			Id = GenerateUniqueId();
		}

		// Factory method that creates an Ant with a random birthdate between 1 and 7 days ago
		public static Ant CreateWithRandomBirthDate(DateTime currentDate)
		{
			int randomDaysAgo = _random.Next(1, 22); // Random number between 1 and 21 days ago
			DateTime birthDate = currentDate.AddDays(-randomDaysAgo);
			return new Ant(birthDate);
		}

		private string GenerateUniqueId()
		{
			return Guid.NewGuid().ToString("N");
		}

		public bool IsAlive(DateTime currentDate)
		{
			// Calculate the age and check if it exceeds the lifespan
			return (currentDate - BirthDate).TotalDays <= LifeSpanInDays;
		}

		public override string ToString()
		{
			return $"ID: {Id}, BirthDate: {BirthDate}, Safety shoes: {HasSafetyShoes}";
		}

		public string ToString(DateTime currentDate)
		{
			return $"ID: {Id}, Alive: {IsAlive(currentDate)}, BirthDate: {BirthDate}, Safety shoes: {HasSafetyShoes}";
		}
	}
}
