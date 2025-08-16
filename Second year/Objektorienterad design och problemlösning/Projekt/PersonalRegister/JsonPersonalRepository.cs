using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace PJU
{
	public class JsonPersonalRepository<T> : IRepository<T> where T : class
	{
		private readonly string _filePath;
		private Dictionary<string, T> _entities;

		private readonly JsonSerializerOptions _options = new JsonSerializerOptions
		{
			WriteIndented = true,
			DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingDefault,
			Converters = { new JsonDateTimeConverter("yyyy-MM-dd") }
		};

		public JsonPersonalRepository(string fileName)
		{
			_filePath = System.IO.Path.Combine(Environment.CurrentDirectory, fileName);
			_entities = new Dictionary<string, T>();
			LoadFromFile();
		}

		public Task AddAsync(T item)
		{
			var entity = (dynamic)item;
			_entities[entity.Id] = item;
			return Task.CompletedTask;
		}

		public Task DeleteAsync(string id)
		{
			_entities.Remove(id);
			return Task.CompletedTask;
		}

		public Dictionary<string, T> GetAll()
		{
			return _entities;
		}

		public T GetById(string id)
		{
			_entities.TryGetValue(id, out var entity);
			return entity;
		}

		public Task UpdateAsync(T item)
		{
			var entity = (dynamic)item;
			_entities[entity.Id] = item;
			return Task.CompletedTask;
		}

		public async Task SaveToFileAsync()
		{
			var json = JsonSerializer.Serialize(_entities, _options);
			await System.IO.File.WriteAllTextAsync(_filePath, json);
		}

		public async Task<int> RemoveDeadPersonalAsync(Func<T, bool> isAlive)
		{
			int initialCount = _entities.Count;
			var deadEntities = _entities.Where(e => !isAlive(e.Value)).Select(e => e.Key).ToList();

			foreach (var id in deadEntities)
			{
				_entities.Remove(id);
			}

			await Task.CompletedTask;
			return initialCount - _entities.Count; // Return number of dead entities
		}

		public async Task AddNewPersonalAsync(Func<T> createNew, int count)
		{
			for (int i = 0; i < count; i++)
			{
				var newEntity = createNew();
				var entity = (dynamic)newEntity;
				_entities[entity.Id] = newEntity;
			}
			await Task.CompletedTask;
		}

		private void LoadFromFile()
		{
			if (System.IO.File.Exists(_filePath))
			{
				var json = System.IO.File.ReadAllText(_filePath);
				_entities = JsonSerializer.Deserialize<Dictionary<string, T>>(json) ?? new Dictionary<string, T>();
			}
		}
	}
}
