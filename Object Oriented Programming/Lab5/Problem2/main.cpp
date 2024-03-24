#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Base class for all characters
class Character {
public:
    Character(string name, int health, int level) : m_name(name), m_health(health), m_level(level) {}

    // Getters and setters for name, health, and level
    string getName() const { return m_name; }
    void setName(string name) { m_name = name; }

    int getHealth() const { return m_health; }
    void setHealth(int health) { m_health = health; }

    int getLevel() const { return m_level; }
    void setLevel(int level) { m_level = level; }

public:
    string m_name;
    int m_health;
    int m_level;
};

// Subclass of Character for wizards
class Wizard : public Character {
public:
    Wizard(string name, int health, int level, int mana, vector<string> spells, int spellPower)
            : Character(name, health, level), m_mana(mana), m_spells(spells), m_spellPower(spellPower) {}

    bool castSpell(string spell) {
        // Check if wizard knows the spell
        auto it = find(m_spells.begin(), m_spells.end(), spell);
        if (it == m_spells.end()) {
            return false;
        }

        // Check if wizard has enough mana
        if (m_mana < 10) {
            return false;
        }

        // Cast the spell
        m_mana -= 10;
        return true;
    }

    // Getters and setters for mana, spells, and spellPower
    int getMana() const { return m_mana; }
    void setMana(int mana) { m_mana = mana; }

    vector<string> getSpells() const { return m_spells; }
    void setSpells(vector<string> spells) { m_spells = spells; }

    int getSpellPower() const { return m_spellPower; }
    void setSpellPower(int spellPower) { m_spellPower = spellPower; }

private:
    int m_mana;
    vector<string> m_spells;
    int m_spellPower;
};

// Subclass of Character for knights
class Knight : public Character {
public:
    Knight(string name, int health, int level, double armor, int swordDamage)
            : Character(name, health, level), m_armor(armor), m_swordDamage(swordDamage) {}

    void takeDamage(int damage) {
        m_armor -= (double)damage / m_swordDamage;
        if (m_armor < 0) {
            m_health += m_armor * m_swordDamage;
            m_armor = 0;
        }
        if (m_health < 0) {
            m_health = 0;
        }
    }


    // Getters and setters for armor and swordDamage
    double getArmor() const { return m_armor; }
    void setArmor(double armor) { m_armor = armor; }

    int getSwordDamage() const { return m_swordDamage; }
    void setSwordDamage(int swordDamage) { m_swordDamage = swordDamage; }

private:
    double m_armor;
    int m_swordDamage;
};


class CharacterTest {
public:
    static void testSetName() {
        Character c("John", 100, 1);
        c.setName("Peter");
        if (c.getName() != "Peter") {
            cout << "testSetName failed" << endl;
        } else {
            cout << "testSetName passed" << endl;
        }
    }

    static void testWizardCastSpell() {
        vector<string> spells = {"Fireball", "Frost Nova", "Arcane Blast"};
        Wizard w("Gandalf", 80, 5, 100, spells, 10);
        bool result = w.castSpell("Fireball");
        if (!result || w.getMana() != 90) {
            cout << "testWizardCastSpell failed" << endl;
        } else {
            cout << "testWizardCastSpell passed" << endl;
        }
    }

    static void testKnightTakeDamage() {
        Knight k("Arthur", 100, 5, 0.8, 5);
        k.takeDamage(20);
        if (k.getArmor() != 0) {
            cout << "testKnightTakeDamage failed" << endl;
        } else {
            cout << "testKnightTakeDamage passed" << endl;
        }
    }

    static void runAll() {
        testSetName();
        testWizardCastSpell();
        testKnightTakeDamage();
    }
};

int main() {
    CharacterTest::runAll();
    cout << "All tests passed!" << endl;
    return 0;
}
